"""Coleta dados abertos do Senado Federal para a Base 3 (saliência dos ministros do STF).

Gera, em dados/brutos/senado/:
  - pets.json            petições (sigla PET) por ano, 2015-2026
  - speeches.json.gz     discursos em plenário, mês a mês (o serviço só devolve dados a partir de mar. 2017)

Uso (da raiz do repositório):  python3 scripts/senado_coleta.py
Rodado originalmente em 2 nov. 2026. Rodar de novo atualiza a série, mas os números da Base 3 foram
calculados com a coleta original; registre a data se refizer.
"""
import calendar, gzip, json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "brutos" / "senado"
OUT.mkdir(parents=True, exist_ok=True)
H = {"Accept": "application/json"}
ULTIMO_MES = (2026, 10)


def get(url):
    for _ in range(4):
        try:
            req = urllib.request.Request(url, headers=H)
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry", url, e, file=sys.stderr)
            time.sleep(4)
    return None


def petições():
    pets = []
    for y in range(2015, ULTIMO_MES[0] + 1):
        d = get(f"https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?sigla=PET&ano={y}")
        try:
            ms = d["PesquisaBasicaMateria"]["Materias"]["Materia"]
        except Exception:  # noqa: BLE001
            ms = []
        if isinstance(ms, dict):
            ms = [ms]
        for m in ms:
            pets.append({k: m.get(k) for k in ["Codigo", "DescricaoIdentificacao", "Ano", "Ementa", "Autor", "Data"]})
        print("PET", y, len(ms), file=sys.stderr)
        time.sleep(0.3)
    json.dump(pets, open(OUT / "pets.json", "w"), ensure_ascii=False, indent=1)
    return pets


def discursos():
    speeches = []
    for y in range(2015, ULTIMO_MES[0] + 1):
        for mth in range(1, 13):
            if (y, mth) > ULTIMO_MES:
                break
            last = calendar.monthrange(y, mth)[1]
            d = get(f"https://legis.senado.leg.br/dadosabertos/plenario/lista/discursos/{y}{mth:02d}01/{y}{mth:02d}{last:02d}")
            try:
                ss = d["DiscursosSessao"]["Sessoes"]["Sessao"]
            except Exception:  # noqa: BLE001
                ss = []
            if isinstance(ss, dict):
                ss = [ss]
            n = 0
            for s in ss:
                ps = (s.get("Pronunciamentos") or {}).get("Pronunciamento", [])
                if isinstance(ps, dict):
                    ps = [ps]
                for p in ps:
                    parl = p.get("Parlamentar") if isinstance(p.get("Parlamentar"), dict) else {}
                    speeches.append({
                        "id": p.get("CodigoPronunciamento"),
                        "data": p.get("Data") or s.get("DataSessao"),
                        "resumo": p.get("Resumo") or "",
                        "index": p.get("Indexacao") or "",
                        "orador": parl.get("NomeParlamentar"),
                        "partido": parl.get("SiglaPartidoParlamentar"),
                    })
                    n += 1
            print("DISC", y, mth, n, file=sys.stderr)
            time.sleep(0.3)
    with gzip.open(OUT / "speeches.json.gz", "wt", encoding="utf-8") as f:
        json.dump(speeches, f, ensure_ascii=False)
    return speeches


if __name__ == "__main__":
    p = petições()
    s = discursos()
    print(len(p), "petições;", len(s), "discursos")
