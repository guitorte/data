"""Etapa 2.6 (parte 2): o teste da P2, nas definições do protocolo e dos desvios 1 a 7.

Lê a classificação, os requerimentos e as tramitações. Grava:
  dados/processados/urgencias_esperas.csv   uma linha por PL (grupo, data da urgência, deliberação, espera, censura)
  dados/processados/urgencias_resultado.json  medianas, percentis, regra de decisão, segunda linha e controle de qualidade
Uso (da raiz):  python3 scripts/urgencias_teste.py
"""
import csv, datetime as dt, gzip, json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
U = ROOT / "dados/brutos/urgencias"; PROC = ROOT / "dados/processados"
CORTE = dt.date(2026, 10, 31)
DELIB = {1235, 1236, 244, 197, 1500, 128, 608, 609}
GRUPO_B = {221, 234, 250, 1008, 223, 1232, 420, 1038}
D = dt.date.fromisoformat

def grupo_b(e):
    desp = (e.get("despacho") or "").lower()
    return int(e["codTipoTramitacao"]) in GRUPO_B or ("retirad" in desp and "de pauta" in desp)

janelas = []
for r in csv.DictReader(open(ROOT / "dados/referencia/calendario_eleitoral.csv")):
    janelas.append((D(r["primeiro_turno"]) - dt.timedelta(days=90), D(r["segundo_turno"])))
def em_janela(d): return any(a <= d <= b for a, b in janelas)

cls = {r["pl"]: r for r in csv.DictReader(open(PROC / "urgencias_classificacao.csv")) if r["grupo"] != "sem_ficha"}
reqs = json.load(open(U / "requerimentos.json"))
urg = {}
for r in reqs.values():
    d = D(r["votacao"]["data"][:10])
    for pl in r.get("alvos", []):
        if pl in cls and (pl not in urg or d < urg[pl]): urg[pl] = d

linhas = []
for pl, c in cls.items():
    if pl not in urg: continue
    ev = json.load(gzip.open(U / "tramitacoes" / f"{c['id']}.json.gz", "rt"))
    ev.sort(key=lambda e: (e["dataHora"], e.get("sequencia") or 0))
    u = urg[pl]
    delib = next((D(e["dataHora"][:10]) for e in ev if int(e["codTipoTramitacao"]) in DELIB and D(e["dataHora"][:10]) >= u), None)
    adi = [D(e["dataHora"][:10]) for e in ev if grupo_b(e) and e.get("siglaOrgao") == "PLEN"]
    tem196 = any(int(e["codTipoTramitacao"]) == 196 and u <= D(e["dataHora"][:10]) <= u + dt.timedelta(days=7) for e in ev)
    fim = delib or CORTE
    linhas.append({"pl": pl, "id": c["id"], "grupo": c["grupo"], "P_conteudo": int(c["P_conteudo"]), "urgencia": u.isoformat(),
                   "deliberacao": delib.isoformat() if delib else "", "espera_dias": (fim - u).days, "censurado": int(delib is None),
                   "adiamentos_plen": len(adi), "adiamentos_em_janela": sum(em_janela(d) for d in adi), "codigo196_ok": int(tem196),
                   "eventos": len(ev)})
with open(PROC / "urgencias_esperas.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0])); w.writeheader(); w.writerows(linhas)

def km_mediana(xs):
    """xs: lista de (tempo, censurado). Mediana de Kaplan-Meier (None se a curva não cai abaixo de 0,5)."""
    s, n = 1.0, len(xs)
    for t in sorted({t for t, c in xs if not c}):
        d = sum(1 for tt, c in xs if tt == t and not c); risco = sum(1 for tt, _ in xs if tt >= t)
        s *= 1 - d / risco
        if s <= 0.5: return t
    return None

def resumo(g):
    xs = [(l["espera_dias"], l["censurado"]) for l in g]
    return {"n": len(g), "mediana_KM_dias": km_mediana(xs), "censurados": sum(c for _, c in xs),
            "deliberados_em_ate_30_dias": sum(1 for t, c in xs if not c and t <= 30)}

def percentis(alvo, ref):
    out = []
    for l in alvo:
        x, cx = l["espera_dias"], l["censurado"]
        inf = sum(1 for r in ref if not r["censurado"] and r["espera_dias"] < x) / len(ref)
        sup = 1.0 if cx else sum(1 for r in ref if r["espera_dias"] < x) / len(ref)
        leitura = "acima_P75" if inf > 0.75 else ("ate_P75" if sup <= 0.75 else "indeterminado")
        out.append({"pl": l["pl"], "espera_dias": x, "censurado": cx, "pct_inf": round(inf, 3), "pct_sup": round(sup, 3), "leitura": leitura})
    return out

def decisao(ps):
    n = len(ps); a = sum(p["leitura"] == "acima_P75" for p in ps); b = sum(p["leitura"] == "ate_P75" for p in ps)
    if n < 3: return "sem força de teste"
    if a > n / 2: return "compatível com estratégia"
    if b > n / 2: return "compatível com complexidade"
    return "inconclusivo"

P = [l for l in linhas if l["grupo"] == "P"]; C = [l for l in linhas if l["grupo"] == "C"]; G = [l for l in linhas if l["grupo"] == "G"]
Pc = [l for l in P if l["P_conteudo"]]
sem2630 = lambda xs: [l for l in xs if l["pl"] != "PL 2630/2020"]
res = {"populacao": len(linhas), "grupos": {"P": resumo(P), "P_sem_2630": resumo(sem2630(P)), "P_conteudo": resumo(Pc),
        "P_conteudo_sem_2630": resumo(sem2630(Pc)), "C": resumo(C), "G": resumo(G)}}
for nome, alvo in [("P", P), ("P_sem_2630", sem2630(P)), ("P_conteudo", Pc), ("P_conteudo_sem_2630", sem2630(Pc))]:
    for refn, ref in [("C", C), ("G", G)]:
        ps = percentis(alvo, ref)
        res[f"{nome}_vs_{refn}"] = {"decisao": decisao(ps), "projetos": ps}
def seg(g):
    a = sum(l["adiamentos_plen"] for l in g); j = sum(l["adiamentos_em_janela"] for l in g)
    return {"adiamentos": a, "em_janela": j, "parcela": round(j / a, 3) if a else None}
res["segunda_linha"] = {"P": seg(P), "P_sem_2630": seg(sem2630(P)), "C": seg(C), "G": seg(G), "esperado_por_acaso": "cerca de 1/6"}
random.seed(2026); amostra = random.sample(linhas, 20)
res["qc_a"] = {"amostra": [l["pl"] for l in amostra], "com_196_na_data": sum(l["codigo196_ok"] for l in amostra),
               "toda_populacao_com_196": sum(l["codigo196_ok"] for l in linhas)}
json.dump(res, open(PROC / "urgencias_resultado.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: res[k] for k in ["populacao", "grupos", "segunda_linha", "qc_a"]}, ensure_ascii=False, indent=1))
for k in ["P_vs_C", "P_sem_2630_vs_C", "P_conteudo_vs_C", "P_conteudo_sem_2630_vs_C", "P_vs_G"]:
    print(k, "→", res[k]["decisao"])
