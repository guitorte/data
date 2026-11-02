"""Etapa 2.5 (parte 2): classificação dos PLs da população pela regra P e pela regra C do protocolo.

Usa SÓ a ementa e a indexação (keywords) de dados/brutos/urgencias/pls_alvo.json. Não lê tramitação nem
desfecho. Grava dados/processados/urgencias_classificacao.csv com:
  pl, ementa, termos_P (filtro 1), candidato_P, decisao_P (filtro 2, preenchida à mão em
  dados/referencia/urgencias_decisoes_P.csv), regra_C, grupo final (P, C ou G)
Uso (da raiz):  python3 scripts/urgencias_classifica.py
"""
import csv, json, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn")

TERMOS_P = [r"plataformas? digita", r"redes? socia", r"provedor(es)? de aplica", r"aplicacoes de internet",
            r"mensageria", r"mensage(m|ns) instantanea", r"ferramentas? de busca", r"buscador",
            r"marco civil da internet", r"lei n[o.º ]*\s*12\.?965", r"desinformacao", r"noticias falsas", r"fake news",
            r"moderacao de conteudo", r"conteudos? gerados? por terceiros"]
TERMOS_C = [r"marco legal", r"\bcodigo\b", r"\bestatuto\b", r"lei geral", r"politica nacional", r"sistema nacional"]

alvos = json.load(open(ROOT / "dados/brutos/urgencias/pls_alvo.json"))
dec_path = ROOT / "dados/referencia/urgencias_decisoes_P.csv"
decisoes = {r["pl"]: r for r in csv.DictReader(open(dec_path))} if dec_path.exists() else {}
rows = []
for pl, f in sorted(alvos.items()):
    f = f or {}
    ementa = f.get("ementa") or ""; idx = f.get("keywords") or ""
    t = norm(ementa + " " + idx)
    termos = [p for p in TERMOS_P if re.search(p, t)]
    c = [p for p in TERMOS_C if re.search(p, norm(ementa))]
    d = decisoes.get(pl, {})
    decP = d.get("decisao_P", "")
    grupo = "P" if decP == "sim" else ("C" if c else "G")
    rows.append({"pl": pl, "id": f.get("id", ""), "ementa": ementa[:400], "termos_P": ";".join(termos),
                 "candidato_P": int(bool(termos)), "decisao_P": decP, "justificativa_P": d.get("justificativa", ""),
                 "regra_C": int(bool(c)), "grupo": grupo})
with open(ROOT / "dados/processados/urgencias_classificacao.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
cand = [r for r in rows if r["candidato_P"]]
print("PLs:", len(rows), "| candidatos P:", len(cand), "| sem decisão:", sum(1 for r in cand if not r["decisao_P"]),
      "| P:", sum(r["grupo"] == "P" for r in rows), "| C:", sum(r["grupo"] == "C" for r in rows),
      "| G:", sum(r["grupo"] == "G" for r in rows))
