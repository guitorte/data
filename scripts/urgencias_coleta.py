"""Etapa 2.5 (parte 1): população do teste da P2.

Coleta as votações do plenário da Câmara mês a mês (fev. 2015 a abr. 2026), separa as aprovações de
requerimento de urgência, chega ao projeto de lei alvo de cada requerimento e baixa a ficha do PL
(ementa e indexação). NÃO baixa tramitações nem desfechos: a classificação (regra P / regra C) é feita e
registrada antes, como manda o protocolo.

Grava em dados/brutos/urgencias/:
  votacoes_plen_AAAA-MM.json.gz   votações do plenário de cada mês (bruto)
  requerimentos.json              ficha de cada requerimento de urgência aprovado
  pls_alvo.json                   ficha de cada PL alvo
Uso (da raiz):  python3 scripts/urgencias_coleta.py
"""
import calendar, gzip, json, re, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "brutos" / "urgencias"; OUT.mkdir(parents=True, exist_ok=True)
B = "https://dadosabertos.camara.leg.br/api/v2"
H = {"Accept": "application/json"}

def get(url):
    for k in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=120) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry", k, url, e, file=sys.stderr); time.sleep(5 * (k + 1))
    return None

def todas(url):
    out = []
    while url:
        d = get(url)
        if d is None: break
        out += d.get("dados", [])
        url = next((l["href"] for l in d.get("links", []) if l.get("rel") == "next"), None)
        time.sleep(0.2)
    return out

URG = re.compile(r"aprovad[oa].{0,40}requerimento.{0,30}urg[eê]ncia|requerimento de urg[eê]ncia.{0,60}aprovad", re.I)

def votacoes():
    urg = []
    for y in range(2015, 2027):
        for m in range(1, 13):
            if (y, m) < (2015, 2) or (y, m) > (2026, 4): continue
            arq = OUT / f"votacoes_plen_{y}-{m:02d}.json.gz"
            if arq.exists():
                v = json.load(gzip.open(arq, "rt"))
            else:
                last = calendar.monthrange(y, m)[1]
                v = todas(f"{B}/votacoes?idOrgao=180&dataInicio={y}-{m:02d}-01&dataFim={y}-{m:02d}-{last}&itens=200")
                json.dump(v, gzip.open(arq, "wt"), ensure_ascii=False)
            u = [x for x in v if URG.search(x.get("descricao") or "") and "rejeitad" not in (x.get("descricao") or "").lower()]
            urg += u
            print(f"{y}-{m:02d} votacoes={len(v)} urgencias={len(u)}", file=sys.stderr)
    return urg

ALVO = re.compile(r"(?:PL|Projeto de Lei)\s*(?:n[º°o.]*\s*)?([\d.]+)\s*/\s*(\d{4})", re.I)

if __name__ == "__main__":
    urg = votacoes()
    reqs = {}
    for x in urg:
        uri = x.get("uriProposicaoObjeto")
        if not uri or uri in reqs: continue
        d = get(uri); reqs[uri] = {"votacao": x, "req": (d or {}).get("dados")}
        time.sleep(0.2)
    json.dump(reqs, open(OUT / "requerimentos.json", "w"), ensure_ascii=False, indent=1)
    alvos = {}
    for uri, r in reqs.items():
        req = r["req"] or {}
        texto = " ".join(filter(None, [req.get("ementa"), (r["votacao"].get("descricao") or "")]))
        cand = ALVO.findall(texto)
        if req.get("siglaTipo") == "PL":  # a própria votação já é sobre um PL
            cand = [(str(req.get("numero")), str(req.get("ano")))]
        r["alvos"] = [f"PL {n.replace('.', '')}/{a}" for n, a in cand]
        for n, a in cand:
            chave = f"PL {n.replace('.', '')}/{a}"
            if chave in alvos: continue
            busca = get(f"{B}/proposicoes?siglaTipo=PL&numero={n.replace('.', '')}&ano={a}")
            ids = [p["id"] for p in (busca or {}).get("dados", [])]
            ficha = get(f"{B}/proposicoes/{ids[0]}") if ids else None
            alvos[chave] = (ficha or {}).get("dados")
            time.sleep(0.2)
    json.dump(reqs, open(OUT / "requerimentos.json", "w"), ensure_ascii=False, indent=1)
    json.dump(alvos, open(OUT / "pls_alvo.json", "w"), ensure_ascii=False, indent=1)
    print("urgencias aprovadas:", len(urg), "| requerimentos:", len(reqs), "| PLs alvo:", len(alvos),
          "| sem alvo:", sum(1 for r in reqs.values() if not r["alvos"]))
