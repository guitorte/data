# A lei como preço

Uma pesquisa sobre o que acontece quando um Estado tenta aplicar a própria lei a uma plataforma digital global e a briga sai do tribunal para o comércio e as sanções entre países.

O caso central é o Brasil. Em 2024, o Supremo suspendeu o X, que cedeu em cinco semanas. O Rumble ficou quase um ano bloqueado sem ceder. Em 2025 e 2026, o governo americano respondeu com tarifas, sanções a um ministro do STF e uma investigação comercial que usou o bloqueio do X como fundamento.

> **Pergunta de trabalho.** Uma multa pontual costuma funcionar como preço: a plataforma paga e segue em frente. O que faz uma plataforma obedecer? E o que acontece quando o governo do país de origem dela compra a briga?

**Situação em 2 nov. 2026.** A pesquisa está em fase exploratória. O rascunho do artigo está parado; o trabalho avança por "expedições" (dossiês e bases de dados) que devem decidir qual pergunta o trabalho responde. O resumo está em [`docs/estado-atual.md`](docs/estado-atual.md).

## Por onde começar

| Se você quer... | Leia |
|---|---|
| saber onde paramos e o que vem agora | [`docs/estado-atual.md`](docs/estado-atual.md) |
| ver o que já sabemos, e com que grau de certeza | [`docs/achados.md`](docs/achados.md) |
| entender a tese e como ela mudou | [`docs/tese-e-hipoteses.md`](docs/tese-e-hipoteses.md) |
| ver o plano | [`ROADMAP.md`](ROADMAP.md) |
| conferir uma fonte | [`fontes/catalogo.md`](fontes/catalogo.md) e a seção "Fontes" de cada base |
| conhecer as regras de pesquisa | [`standards.txt`](standards.txt) (obrigatório) e [`docs/metodo.md`](docs/metodo.md) |

## Mapa do repositório

```
data/                         (este repositório)
├── README.md                 você está aqui
├── ROADMAP.md                fases, expedições e pontos de controle
├── CLAUDE.md                 instruções que o Claude Code lê em toda sessão
├── standards.txt             padrão de citação e evidência do projeto (cópia fiel)
│
├── docs/                     o caderno de campo
│   ├── estado-atual.md       passagem de turno: onde paramos, o que falta decidir
│   ├── achados.md            balanço dos achados (estabelecido, sustentado, contestado, em aberto)
│   ├── tese-e-hipoteses.md   tese, hipóteses, histórico e as 17 suspeitas "e se"
│   ├── decisoes.md           registro datado das decisões
│   ├── previsoes.md          previsões feitas antes dos dados
│   ├── metodo.md             testes, marcações, medidas e limites
│   └── conversas/            resumos das conversas que produziram o material
│
├── manuscrito/               o texto do artigo (parado desde 2 nov. 2026)
│   ├── rascunho-artigo.md    seções 1 a 10, 69 notas e as referências
│   └── esqueleto-projeto.md  a primeira camada do projeto
│
├── dossies/                  investigações fechadas sobre um tema
│   ├── secao-301.md          o processo comercial americano contra o Brasil
│   └── linha-do-tempo-brasil-eua.md   47 eventos, 2024 a 2026
│
├── bases/                    uma linha por caso, com campos fixos
│   ├── base1-aplicacao-no-brasil.md      ordens contra plataformas no Brasil
│   ├── base2-instrumentos-pais-sede.md   medidas dos EUA contra regulação de plataformas no exterior
│   └── base3-saliencia-ministros.md      ministros do STF nos discursos e pedidos do Senado
│
├── dados/
│   ├── brutos/               o que veio das APIs, sem edição
│   └── processados/          tabelas geradas pelos scripts
├── scripts/                  coleta e análise reproduzíveis (Python 3, só biblioteca padrão)
│
├── fontes/
│   ├── catalogo.md           o que foi consultado, de onde veio e para que serviu
│   ├── livros.md             os livros usados (os arquivos ficam fora do repositório)
│   ├── primarias-eua/        documentos do governo americano (domínio público)
│   └── textos-extraidos/     versão em texto dos documentos longos, para busca
│
├── referencias/              a lista inicial de referências (os códigos U# do esqueleto)
└── notebooklm/               o prompt e as perguntas para o caderno do NotebookLM
```

## Como trabalhar com o Claude Code

O repositório foi organizado para que uma conversa nova comece de onde a anterior parou, sem depender da memória de ninguém.

- **No início de cada sessão:** "Leia o `docs/estado-atual.md` e me diga onde paramos." O `CLAUDE.md` é lido automaticamente e traz as regras do projeto.
- **Durante:** cada expedição deixa três rastros (dados, fontes e texto); o `CLAUDE.md` diz onde cada um vai.
- **No fim:** "Atualize o `estado-atual.md` e faça o commit." O histórico do Git passa a ser o diário da pesquisa.

Os dados se refazem da raiz do repositório:

```bash
python3 scripts/senado_analise.py      # refaz as tabelas da Base 3 a partir de dados/brutos/senado
python3 scripts/senado_coleta.py       # baixa de novo os dados do Senado (demora; muda os números)
python3 scripts/lda_coleta.py brasil   # registros de lobby nos EUA que citam o Brasil
```

## O que não está aqui

- **Os livros.** Por direito autoral, ficam na pasta "Pdfs" do Google Drive. A lista está em [`fontes/livros.md`](fontes/livros.md).
- **Documentos de terceiros com direitos,** como os comentários da CCIA ao USTR. O catálogo traz o link.
- **A conversa original.** Ela fica no Claude, no projeto "Arguments". O resumo está em [`docs/conversas/`](docs/conversas/).
- **O documento no Claude Docs** ("A lei como preço"), de onde as abas foram exportadas em 2 nov. 2026. Ele continua existindo como versão de leitura: <https://claude.ai/artifact/5pWrJrL1Q2djw6q515Cajt>.

O repositório é **público**, por decisão do autor em 2 nov. 2026. Ele contém um artigo em andamento e notas de trabalho.
