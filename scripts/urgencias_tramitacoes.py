"""Etapa 2.6 (parte 1): baixa a tramitação na Câmara de cada PL da população (exceto sem_ficha).
Grava dados/brutos/urgencias/tramitacoes/{id}.json.gz (cache: não baixa de novo o que já existe).
Uso (da raiz):  python3 scripts/urgencias_tramitacoes.py
"""
import csv, gzip, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from urgencias_coleta import get, B, OUT  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
T = OUT / "tramitacoes"; T.mkdir(exist_ok=True)
rows = [r for r in csv.DictReader(open(ROOT / "dados/processados/urgencias_classificacao.csv")) if r["grupo"] != "sem_ficha"]
feitos = 0
for i, r in enumerate(rows):
    arq = T / f"{r['id']}.json.gz"
    if arq.exists(): continue
    d = get(f"{B}/proposicoes/{r['id']}/tramitacoes")
    json.dump((d or {}).get("dados", []), gzip.open(arq, "wt"), ensure_ascii=False)
    feitos += 1; time.sleep(0.15)
    if i % 100 == 0: print(i, "de", len(rows), file=sys.stderr, flush=True)
print("PLs:", len(rows), "| baixados agora:", feitos)
