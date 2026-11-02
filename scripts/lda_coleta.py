"""Registros de lobby nos EUA (Lobbying Disclosure Act, API pública lda.gov) usados no Dossiê Seção 301.

Gera em dados/brutos/lda/:
  - lda_brazil.json   relatórios de 2024-2026 cujo campo de questões específicas menciona "Brazil"
  - lda_clients.json  trechos sobre censura/301/Brasil/DSA nos relatórios de 2025 de clientes selecionados

Uso (da raiz):  python3 scripts/lda_coleta.py [brasil|clientes]
Cuidado conhecido: o filtro por nome de cliente traz falsos positivos (ex.: "Metal" casa com "META");
foram ignorados na análise.
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "brutos" / "lda"
OUT.mkdir(parents=True, exist_ok=True)


def fetch(url):
    for _ in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry", e, file=sys.stderr); time.sleep(5)
    return None


def brasil():
    out = []
    for year in (2024, 2025, 2026):
        url = f"https://lda.gov/api/v1/filings/?filing_specific_lobbying_issues=Brazil&filing_year={year}&page_size=25"
        while url:
            d = fetch(url)
            if d is None:
                break
            for f in d["results"]:
                acts = []
                for a in f.get("lobbying_activities", []):
                    desc = a.get("description") or ""
                    if "brazil" in desc.lower():
                        acts.append({"issue": a.get("general_issue_code_display"), "desc": desc,
                                     "gov": [g.get("name") for g in a.get("government_entities", [])]})
                out.append({"year": f["filing_year"], "period": f["filing_period_display"], "type": f["filing_type_display"],
                            "registrant": f["registrant"]["name"], "client": f["client"]["name"],
                            "income": f.get("income"), "expenses": f.get("expenses"),
                            "url": f["filing_document_url"], "acts": acts})
            url = d.get("next"); time.sleep(0.5)
    json.dump(out, open(OUT / "lda_brazil.json", "w"), ensure_ascii=False, indent=1)
    print(len(out), "relatórios")


def clientes():
    clients = ["X Corp", "Rumble", "Trump Media", "Computer & Communications Industry Association", "NetChoice",
               "Meta Platforms", "Google"]
    pat = r"censor|301|speech|brazil|foreign (?:government|digital|content)|DSA|digital services act"
    res = {}
    for c in clients:
        url = "https://lda.gov/api/v1/filings/?" + urllib.parse.urlencode({"client_name": c, "filing_year": 2025, "page_size": 25})
        rows, pages = [], 0
        while url and pages < 6:
            d = fetch(url); pages += 1
            if d is None:
                continue
            for f in d["results"]:
                for a in f.get("lobbying_activities", []):
                    desc = a.get("description") or ""
                    sents = [s.strip() for s in re.split(r"(?<=[.;\n])\s+", desc) if re.search(pat, s, re.I)]
                    if sents:
                        rows.append((f["client"]["name"], f["registrant"]["name"], f["filing_period_display"],
                                     " || ".join(sents)[:300]))
            url = d.get("next"); time.sleep(0.4)
        res[c] = sorted(set(rows))
        print(c, len(res[c]))
    json.dump({k: list(v) for k, v in res.items()}, open(OUT / "lda_clients.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "brasil"
    {"brasil": brasil, "clientes": clientes}[modo]()
