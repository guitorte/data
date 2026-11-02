"""Análise da Base 3: petições contra ministros do STF e menções em discursos do Senado.

Lê dados/brutos/senado/ e grava em dados/processados/:
  - senado_peticoes_contra_ministros_STF.csv
  - speeches_by_year.csv
  - senado_discursos_mensal.csv                    (inclui contagem de palavras, para normalizar por 10 mil palavras)
  - senado_mencoes_por_10mil_palavras_anual.csv  (Tabela 2 da Base 3: ocorrências por 10 mil palavras)
  - senado_discursos_impeachment_ministros_mensal.csv (versão estrita: impeachment/crime de responsabilidade
                                                       e STF/ministro no mesmo trecho; precisão ~3/4 numa amostra de 12)

Uso (da raiz):  python3 scripts/senado_analise.py
Reúne o código usado em 2 nov. 2026, que estava espalhado em comandos avulsos. As medidas usam o resumo
e a indexação feitos pela equipe do Senado, não o texto integral. Nomes com * são ministros nomeados a partir
de 2020-2023 e entram só na contagem por nome (a regex pode pegar homônimos).
"""
import collections, csv, gzip, json, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRUTOS = ROOT / "dados" / "brutos" / "senado"
PROC = ROOT / "dados" / "processados"
PROC.mkdir(parents=True, exist_ok=True)


def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn")


NOMES = {"Moraes": r"alexandre de moraes", "Gilmar Mendes": r"gilmar mendes", "Toffoli": r"toffoli",
         "Barroso": r"barroso", "Fachin": r"fachin", "Fux": r"\bfux\b", "Carmen Lucia": r"carmen lucia",
         "Rosa Weber": r"rosa weber", "Lewandowski": r"lewandowski", "Celso de Mello": r"celso de mello",
         "Marco Aurelio": r"marco aurelio mello", "Teori": r"teori", "Nunes Marques": r"nunes marques|kassio",
         "Andre Mendonca*": r"andre mendonca", "Zanin*": r"zanin", "Flavio Dino*": r"flavio dino"}
STF = re.compile(r"supremo tribunal federal|\bstf\b")
MINISTROS_ESTRITO = (r"alexandre de moraes|gilmar mendes|toffoli|barroso|fachin|\bfux\b|carmen lucia|rosa weber|"
                     r"lewandowski|celso de mello|marco aurelio mello|teori|nunes marques|kassio")
ALVO_IMP = MINISTROS_ESTRITO + r"|ministros? do supremo|supremo tribunal federal|\bstf\b"
IMP = r"impeachment|crime de responsabilidade"


def peticoes():
    pets = json.load(open(BRUTOS / "pets.json"))
    py = collections.defaultdict(collections.Counter)
    rows = []
    for p in pets:
        e = norm(p["Ementa"]); y = p["Ano"]
        py[y]["total"] += 1
        if STF.search(e) or any(re.search(v, e) for v in NOMES.values()):
            py[y]["stf"] += 1
            hit = [k for k, v in NOMES.items() if re.search(v, e)]
            if "11 ministros" in e or "todos os ministros" in e or "ministros do supremo" in e:
                hit.append("varios/todos")
            for h in hit:
                py[y][h] += 1
            rows.append((y, p["DescricaoIdentificacao"], p["Data"], ";".join(hit), p["Ementa"][:180]))
    with open(PROC / "senado_peticoes_contra_ministros_STF.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["ano", "identificacao", "data", "ministros", "ementa"]); w.writerows(rows)
    print("PET por ano: total | contra ministros do STF | Moraes")
    for y in sorted(py):
        print(y, py[y]["total"], py[y]["stf"], py[y]["Moraes"])


def discursos():
    with gzip.open(BRUTOS / "speeches.json.gz", "rt", encoding="utf-8") as f:
        sp = json.load(f)
    seen = set()
    anual = collections.defaultdict(collections.Counter)
    mensal = collections.defaultdict(collections.Counter)
    imp_mensal = collections.Counter()
    for s in sp:
        if s["id"] in seen:
            continue
        seen.add(s["id"])
        d = s["data"] or ""; y = d[:4]; ym = d[:7]
        t = norm(s["resumo"] + " " + s["index"])
        # anual
        a = anual[y]; a["total"] += 1
        if STF.search(t): a["stf"] += 1
        hits = [k for k, v in NOMES.items() if re.search(v, t)]
        if [h for h in hits if not h.endswith("*")]: a["any_min_strict"] += 1
        for h in hits: a[h] += 1
        # mensal
        m = mensal[ym]
        m["discursos"] += 1; m["palavras"] += len(t.split())
        m["com_stf"] += bool(STF.search(t))
        m["com_ministro"] += bool(re.search(MINISTROS_ESTRITO, t))
        m["com_moraes"] += bool(re.search("alexandre de moraes", t))
        # impeachment, versão estrita (mesmo trecho)
        segs = [norm(s["resumo"])] + [norm(x) for x in re.split(r"\n\s*\n", s["index"] or "")]
        if any(re.search(IMP, g) and re.search(ALVO_IMP, g) for g in segs):
            imp_mensal[ym] += 1
    with open(PROC / "speeches_by_year.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ano", "discursos", "pct_stf", "pct_ministro", "moraes", "gilmar", "toffoli", "barroso", "fachin",
                    "fux", "mendonca*", "dino*", "zanin*", "n_stf", "n_ministro"])
        for y in sorted(anual):
            c = anual[y]; tot = c["total"]
            w.writerow([y, tot, round(100 * c["stf"] / tot, 2), round(100 * c["any_min_strict"] / tot, 2), c["Moraes"],
                        c["Gilmar Mendes"], c["Toffoli"], c["Barroso"], c["Fachin"], c["Fux"], c["Andre Mendonca*"],
                        c["Flavio Dino*"], c["Zanin*"], c["stf"], c["any_min_strict"]])
    with open(PROC / "senado_discursos_mensal.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["mes", "discursos", "palavras_resumo_indexacao", "discursos_com_STF",
                    "discursos_com_ministro_nominal", "discursos_com_Moraes"])
        for ym in sorted(mensal):
            r = mensal[ym]
            w.writerow([ym, r["discursos"], r["palavras"], r["com_stf"], r["com_ministro"], r["com_moraes"]])
    with open(PROC / "senado_discursos_impeachment_ministros_mensal.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["mes", "discursos_que_associam_impeachment_a_ministros_ou_STF"])
        for k, v in sorted(imp_mensal.items()):
            w.writerow([k, v])
    # Tabela 2 da Base 3: OCORRÊNCIAS (não discursos) por 10 mil palavras, por ano
    W = collections.Counter(); S = collections.Counter(); N = collections.Counter(); Mo = collections.Counter()
    seen = set()
    for s in sp:
        if s["id"] in seen:
            continue
        seen.add(s["id"]); y = (s["data"] or "")[:4]
        t = norm(s["resumo"] + " " + s["index"])
        W[y] += len(t.split())
        S[y] += len(re.findall(r"supremo tribunal federal|\bstf\b", t))
        N[y] += len(re.findall(MINISTROS_ESTRITO, t))
        Mo[y] += len(re.findall("alexandre de moraes", t))
    with open(PROC / "senado_mencoes_por_10mil_palavras_anual.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ano", "palavras_resumo_indexacao", "mencoes_STF_por_10mil", "mencoes_ministros_por_10mil",
                    "mencoes_Moraes_por_10mil"])
        for y in sorted(W):
            w.writerow([y, W[y], round(1e4 * S[y] / W[y], 1), round(1e4 * N[y] / W[y], 1), round(1e4 * Mo[y] / W[y], 2)])
    print("ano | menções STF/10 mil palavras | ministros/10 mil | Moraes/10 mil")
    for y in sorted(W):
        print(y, round(1e4 * S[y] / W[y], 1), round(1e4 * N[y] / W[y], 1), round(1e4 * Mo[y] / W[y], 2))

if __name__ == "__main__":
    peticoes()
    discursos()
