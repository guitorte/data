# Estudo de caso: a tramitação do PL 2630/2020

Etapas 2.2 e 2.3 da expedição da tramitação, com as definições do protocolo aprovado em 2 nov. 2026 (`docs/protocolos/tramitacao.md`). Este é o **estudo de caso**, não o teste da P2. O PL 2630 não é cego: já sabíamos parte da história antes dos dados.

## Em uma frase

O projeto passou no Senado em 51 dias. Na Câmara, em mais de seis anos, registrou só dois andamentos formais: a urgência aprovada em 25 abr. 2023 e a retirada de pauta uma semana depois. Desde então está parado há mais de três anos e meio, sem votação.

## Os números (coleta de 2 nov. 2026; corte em 31 out. 2026)

| Medida (definições do protocolo) | Valor |
|---|---|
| Senado: da apresentação (13 maio 2020) à remessa à Câmara (3 jul. 2020) | 51 dias |
| Câmara: eventos de tramitação registrados | 76 (grupo A: 2; grupo B: 1; grupo C: 73) |
| Último evento de andamento (grupos A ou B) | 2 maio 2023 |
| Último evento de qualquer tipo | 24 abr. 2024 (pedido de apensação) |
| Espera desde a urgência aprovada (25 abr. 2023) | 1.285 dias, **censurado** (sem votação até o corte) |
| Fração da vida na Câmara em intervalos parados de 180 dias ou mais | 99,7% (99,6% descontados os recessos) |
| Maior intervalo parado | 2 maio 2023 a 31 out. 2026: 1.278 dias, ainda aberto |
| Adiamentos no plenário (grupo B) | 1: "Retirado de pauta, de ofício", 2 maio 2023, fora de janela eleitoral |

**Estabelecido** (dados oficiais da Câmara e do Senado): os números acima, dentro das definições do protocolo.

## Como ler, com cuidado

- **"Parado" quer dizer sem andamento formal registrado.** De jul. 2020 a abr. 2023, o registro tem quase só apensações e requerimentos (grupo C). Discussões fora dos ritos formais, como grupos de trabalho, não aparecem na tramitação do projeto. Que houve um grupo de trabalho sobre o PL 2630 em 2021 é lembrança de memória, a conferir; se houve, a fração de 99,7% superestima a inércia real. **Em aberto.**
- **O registro da Câmara tem falhas que importam.**
  - A retirada de pauta de 2 maio 2023 veio com o código "Retirada pelo Autor(a)", mas o despacho diz "Retirado de pauta, de ofício". Valeu o texto (desvio 1 do protocolo).
  - A inclusão em pauta, que sabemos ter ocorrido porque o projeto foi retirado dela, não aparece como evento.
  - Em 6 abr. 2022, um pedido de urgência foi rejeitado no plenário (249 sim, 207 não). Aparece só como "Notificações", num projeto apensado. Fica registrado à parte, como descrição.
- **A janela eleitoral não pegou o único adiamento,** que caiu em maio de 2023, longe de eleição. Com um evento só, isso não diz nada sobre a P2.
- **Um caso só não testa a P2.** O que este caso mostra é a forma do atraso: não houve uma sequência de adiamentos, e sim uma urgência aprovada seguida de silêncio. Inferência nossa: no PL 2630, o atraso funcionou mais como gaveta do que como pauta adiada.

## Fontes e consultas (2 nov. 2026)

- Câmara, ficha e tramitações do PL 2630/2020 (id 2256735): `https://dadosabertos.camara.leg.br/api/v2/proposicoes/2256735` e `.../tramitacoes`. Arquivos em `dados/brutos/tramitacao/`.
- Senado, processo do PL 2630/2020 (id 7914763, matéria 141944): `https://legis.senado.leg.br/dadosabertos/processo/7914763`.
- Calendário eleitoral: `dados/referencia/calendario_eleitoral.csv`. As datas de 2020 vêm da Agência Senado (EC 107); as demais seguem a regra constitucional, citada de memória, porque os sites do TSE e do Planalto bloquearam o acesso automatizado. Ficam a conferir.
- Scripts: `scripts/tramitacao_coleta.py` (2.2) e `scripts/tramitacao_pl2630.py` (2.3). Saídas em `dados/processados/pl2630_*`.

## Próximo passo

Etapa 2.4 (esforço alto): o contexto do único adiamento formal (2 maio 2023), da urgência rejeitada de abr. 2022 e da urgência aprovada sem votação de abr. 2023, segundo as categorias do protocolo.
