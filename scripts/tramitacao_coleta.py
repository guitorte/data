"""Etapa 2.2 da expedição da tramitação: coleta da tramitação do PL 2630/2020.

Grava em dados/brutos/tramitacao/ (data da coleta no nome):
  - camara_pl2630_proposicao_AAAA-MM-DD.json   ficha da proposição (id 2256735)
  - camara_pl2630_tramitacoes_AAAA-MM-DD.json  todos os eventos de tramitação na Câmara
  - senado_pl2630_processo_AAAA-MM-DD.json     processo no Senado (id 7914763, matéria 141944)

Uso (da raiz):  python3 scripts/tramitacao_coleta.py
Protocolo: docs/protocolos/tramitacao.md (aprovado em 2 nov. 2026).
"""
import datetime, json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "brutos" / "tramitacao"
OUT.mkdir(parents=True, exist_ok=True)
HOJE = datetime.date.today().isoformat()
H = {"Accept": "application/json"}
CAMARA = "https://dadosabertos.camara.leg.br/api/v2"
SENADO = "https://legis.senado.leg.br/dadosabertos"


def get(url):
    for _ in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=90) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry", url, e, file=sys.stderr); time.sleep(4)
    raise SystemExit(f"falhou: {url}")


def salvar(nome, dados):
    p = OUT / f"{nome}_{HOJE}.json"
    json.dump(dados, open(p, "w"), ensure_ascii=False, indent=1)
    return p


if __name__ == "__main__":
    prop = get(f"{CAMARA}/proposicoes/2256735")
    tram = get(f"{CAMARA}/proposicoes/2256735/tramitacoes")
    sen = get(f"{SENADO}/processo/7914763")
    for nome, d in [("camara_pl2630_proposicao", prop), ("camara_pl2630_tramitacoes", tram),
                    ("senado_pl2630_processo", sen)]:
        print(salvar(nome, d).name)
    ev = tram.get("dados", [])
    print("eventos na Câmara:", len(ev), "| primeiro:", ev[0]["dataHora"][:10] if ev else "-",
          "| último:", ev[-1]["dataHora"][:10] if ev else "-")
