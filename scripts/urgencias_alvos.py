"""Etapa 2.5 (parte 1b): liga cada requerimento de urgência ao PL alvo, com leitura mais tolerante da ementa.

Correção de coleta (2 nov. 2026): a primeira versão só reconhecia "PL 123/2020" e perdia o formato
"Projeto de Lei nº 1.234, de 2020", usado em centenas de requerimentos. Esta versão:
  1. aceita "nº X/AAAA", "nº X, de AAAA", "nº X de AAAA", "nº X, AAAA" e ano com dois dígitos ("X/25");
  2. ignora "Projeto de Lei Complementar" (PLP, fora da população do protocolo);
  3. para ementas genéricas ("apreciação de proposição"), consulta /proposicoes/{id}/relacionadas.
Reaproveita as fichas já baixadas em pls_alvo.json e só busca as que faltam.
Uso (da raiz):  python3 scripts/urgencias_alvos.py
"""
import json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from urgencias_coleta import get, B, OUT  # noqa: E402

PL_RE = re.compile(r"(?:\bPL\b|Projeto de Lei(?!\s+Complementar))\s*(?:n[º°o.]*\s*)?(\d[\d.]*)\s*(?:/\s*|,?\s*de\s+|,\s*)(\d{4}|\d{2})\b", re.I)

def ano4(a): return a if len(a) == 4 else ("20" + a if int(a) <= 30 else "19" + a)

def alvos_de(texto):
    return sorted({f"PL {n.replace('.', '')}/{ano4(a)}" for n, a in PL_RE.findall(texto or "")})

if __name__ == "__main__":
    reqs = json.load(open(OUT / "requerimentos.json"))
    pls = json.load(open(OUT / "pls_alvo.json")) if (OUT / "pls_alvo.json").exists() else {}
    genericos = 0
    for uri, r in reqs.items():
        req = r["req"] or {}
        al = alvos_de(" ".join(filter(None, [req.get("ementa"), r["votacao"].get("descricao")])))
        if not al and re.search(r"apreciação de (?:proposição|matéria)|regime de urgência para (?:a )?apreciação\.?$", req.get("ementa") or "", re.I):
            genericos += 1
            rel = get(f"{B}/proposicoes/{req.get('id')}/relacionadas") or {}
            al = sorted({f"PL {p['numero']}/{p['ano']}" for p in rel.get("dados", []) if p.get("siglaTipo") == "PL"})
            r["alvo_por_relacionadas"] = True
            time.sleep(0.2)
        r["alvos"] = al
        for chave in al:
            if chave in pls: continue
            n, a = chave[3:].split("/")
            busca = get(f"{B}/proposicoes?siglaTipo=PL&numero={n}&ano={a}")
            ids = [p["id"] for p in (busca or {}).get("dados", [])]
            ficha = get(f"{B}/proposicoes/{ids[0]}") if ids else None
            pls[chave] = (ficha or {}).get("dados")
            time.sleep(0.2)
    json.dump(reqs, open(OUT / "requerimentos.json", "w"), ensure_ascii=False, indent=1)
    json.dump(pls, open(OUT / "pls_alvo.json", "w"), ensure_ascii=False, indent=1)
    com = sum(1 for r in reqs.values() if r["alvos"])
    print("requerimentos:", len(reqs), "| com PL alvo:", com, "| sem PL alvo:", len(reqs) - com,
          "| genéricos consultados:", genericos, "| PLs alvo:", len(pls), "| fichas vazias:", sum(1 for v in pls.values() if not v))
