"""Etapa 2.3: linha do tempo do PL 2630/2020, com as definições do protocolo (docs/protocolos/tramitacao.md).

Lê dados/brutos/tramitacao/ e dados/referencia/calendario_eleitoral.csv. Grava em dados/processados/:
  - pl2630_camara_eventos.csv     cada evento na Câmara, com o grupo do protocolo (A, B ou C)
  - pl2630_camara_intervalos.csv  intervalos entre eventos dos grupos A ou B
  - pl2630_resumo.json            medidas do protocolo para o caso
Uso (da raiz):  python3 scripts/tramitacao_pl2630.py
"""
import csv, datetime as dt, glob, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BR = ROOT / "dados" / "brutos" / "tramitacao"
PROC = ROOT / "dados" / "processados"
CORTE = dt.date(2026, 10, 31)

def faixa(a, b): return set(range(a, b + 1))
GRUPO_A = ({150, 151, 1058, 196, 215, 210, 214, 330, 1040, 120, 121, 122, 1071}
           | faixa(322, 326) | faixa(335, 340) | faixa(1027, 1030)
           | {216, 219, 220, 222, 227, 231, 232, 233, 237, 238, 239, 240, 244, 245, 1231, 1233, 1500} | faixa(1235, 1240)
           | {128, 137, 197, 198, 200, 251, 469, 502, 608, 609, 1012, 1013, 1024, 1025, 1241, 1518, 1519})
GRUPO_B = {221, 234, 250, 1008, 223, 1232, 420, 1038}
DELIB_MERITO = {1235, 1236, 244, 197, 1500, 128, 608, 609}

def grupo(cod, despacho=""):
    # Desvio 1 do protocolo (2 nov. 2026): o texto do despacho prevalece sobre o código quando diz "retirado de pauta"
    if "retirad" in despacho.lower() and "de pauta" in despacho.lower():
        return "B"
    return "B" if cod in GRUPO_B else ("A" if cod in GRUPO_A else "C")

def recesso(d):  # recessos constitucionais (datas de memória; conferir art. 57)
    return (d.month == 7 and 18 <= d.day <= 31) or (d.month == 12 and d.day >= 23) or (d.month == 1) or (d.month == 2 and d.day == 1)

def janelas():
    out = []
    for r in csv.DictReader(open(ROOT / "dados/referencia/calendario_eleitoral.csv")):
        t1 = dt.date.fromisoformat(r["primeiro_turno"]); t2 = dt.date.fromisoformat(r["segundo_turno"])
        out.append((t1 - dt.timedelta(days=90), t2, r["ano"]))
    return out

def na_janela(d, J):
    return next((a for i, f, a in J if i <= d <= f), "")

ev = json.load(open(sorted(glob.glob(str(BR / "camara_pl2630_tramitacoes_*.json")))[-1]))["dados"]
ev.sort(key=lambda e: (e["dataHora"], e["sequencia"]))
J = janelas()
rows = []
for e in ev:
    d = dt.date.fromisoformat(e["dataHora"][:10]); c = int(e["codTipoTramitacao"])
    rows.append({"data": d.isoformat(), "orgao": e["siglaOrgao"], "cod": c, "grupo": grupo(c, e.get("despacho") or ""),
                 "tipo": e["descricaoTramitacao"], "regime": e.get("regime") or "",
                 "janela_eleitoral": na_janela(d, J), "despacho": (e.get("despacho") or "").replace("\n", " ")[:300]})
with open(PROC / "pl2630_camara_eventos.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

inicio = dt.date.fromisoformat(rows[0]["data"])
desfecho = next((r for r in rows if r["cod"] in {251, 128, 1012, 1013, 197, 502, 1024}), None)
fim = dt.date.fromisoformat(desfecho["data"]) if desfecho else CORTE
marcos = sorted({dt.date.fromisoformat(r["data"]) for r in rows if r["grupo"] in "AB"})
marcos_lim = [inicio] + marcos + ([] if desfecho else [CORTE])
marcos_lim = sorted(set(marcos_lim))
interv = []
for a, b in zip(marcos_lim, marcos_lim[1:]):
    dias = (b - a).days
    sem_rec = sum(1 for k in range(dias) if not recesso(a + dt.timedelta(days=k)))
    interv.append({"de": a.isoformat(), "ate": b.isoformat(), "dias": dias, "dias_sem_recesso": sem_rec,
                   "parado_180": int(dias >= 180), "censurado": int(b == CORTE and not desfecho)})
with open(PROC / "pl2630_camara_intervalos.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(interv[0])); w.writeheader(); w.writerows(interv)

vida = (fim - inicio).days
parado = sum(i["dias"] for i in interv if i["parado_180"])
vida_sr = sum(1 for k in range(vida) if not recesso(inicio + dt.timedelta(days=k)))
parado_sr = sum(i["dias_sem_recesso"] for i in interv if i["dias_sem_recesso"] >= 180)
urg = [r for r in rows if r["cod"] == 196]
adiam = [r for r in rows if r["grupo"] == "B" and r["orgao"] == "PLEN"]
pauta = [r for r in rows if r["cod"] in (150, 151)]
delib = [r for r in rows if r["cod"] in DELIB_MERITO]
espera = None
if urg:
    u = dt.date.fromisoformat(urg[-1]["data"])
    d2 = next((dt.date.fromisoformat(r["data"]) for r in delib if r["data"] >= urg[-1]["data"]), None)
    espera = {"urgencia": u.isoformat(), "deliberacao": d2.isoformat() if d2 else None,
              "dias": ((d2 or CORTE) - u).days, "censurado": d2 is None}
res = {"chegada_camara": inicio.isoformat(), "desfecho": desfecho["tipo"] if desfecho else None,
       "fim_observacao": fim.isoformat(), "vida_dias": vida, "eventos": len(rows),
       "eventos_por_grupo": {g: sum(r["grupo"] == g for r in rows) for g in "ABC"},
       "ultimo_evento": rows[-1]["data"], "ultimo_evento_A_ou_B": marcos[-1].isoformat() if marcos else None,
       "tempo_parado_dias": parado, "fracao_parado": round(parado / vida, 3),
       "fracao_parado_sem_recesso": round(parado_sr / vida_sr, 3),
       "maior_intervalo": max(interv, key=lambda i: i["dias"]),
       "urgencias_aprovadas": [r["data"] for r in urg], "espera_urgencia": espera,
       "inclusoes_em_pauta": [r["data"] for r in pauta],
       "adiamentos_plenario": [(r["data"], r["tipo"], r["janela_eleitoral"]) for r in adiam],
       "deliberacoes_merito": [(r["data"], r["tipo"]) for r in delib],
       "urgencias_rejeitadas_descritivo": [(r["data"], r["despacho"][:160]) for r in rows if "rejeitado o requerimento de urg" in r["despacho"].lower()]}
sen = json.load(open(sorted(glob.glob(str(BR / "senado_pl2630_processo_*.json")))[-1]))
inf = sorted(sen["autuacoes"][0]["informesLegislativos"], key=lambda i: i["data"])
rem = sen.get("dataSituacaoAtual")[:10]
res["senado"] = {"primeiro_informe": inf[0]["data"][:10], "remessa_a_camara": rem,
                 "dias_ate_remessa": (dt.date.fromisoformat(rem) - dt.date.fromisoformat(inf[0]["data"][:10])).days,
                 "ultimo_informe": inf[-1]["data"][:10],
                 "informes": len(inf), "situacao": sen.get("situacaoAtual")}
json.dump(res, open(PROC / "pl2630_resumo.json", "w"), ensure_ascii=False, indent=1)
json.dump(res, open(PROC / "pl2630_resumo.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
