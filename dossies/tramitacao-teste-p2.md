# Teste da P2: o atraso na lei sobre plataformas é estratégia ou complexidade?

Etapa 2.6 da expedição da tramitação, feita em 2 nov. 2026 com o protocolo aprovado (`docs/protocolos/tramitacao.md`, desvios 1 a 7). As definições e o script foram registrados no Git **antes** de os desfechos serem baixados.

## Em uma frase

Pela regra registrada, o teste deu **inconclusivo**. Fora da regra, como exploração, os projetos sobre plataformas caem mais vezes na "gaveta" da urgência: 5 de 9 ficaram mais de um ano sem votação, contra cerca de 1 em 4 no controle. A diferença ainda é fraca para afirmar alguma coisa, e o momento dos adiamentos não mostra nenhum padrão eleitoral.

## A população

| | |
|---|---|
| PLs com urgência aprovada no plenário da Câmara (fev. 2015 a abr. 2026) | 1.121 com dados completos |
| De plataforma (regra P literal) | 9, dos quais 6 no subconjunto "conteúdo" |
| Controle complexo (regra C) | 264 |
| Controle geral | 848 |
| Fora | 30 sem ficha; 2 sem data de urgência ligada (PL 1011/2020 e PL 1123/2025) |

**Controle de qualidade (a): passou.** Na amostra aleatória de 20 PLs, todos têm o código de urgência aprovada na tramitação até 7 dias depois da votação. Na população inteira, 1.110 de 1.121 têm.

**Controle de qualidade (b): não feito.** A conferência de vazamentos por busca de palavra-chave ficou pendente.

## Resultado pela regra registrada (medida principal)

Espera = dias entre a urgência aprovada e a primeira votação de mérito no plenário. Projetos não votados até 31 out. 2026 contam como "pelo menos" a espera observada.

| Comparação | Decisão pela regra |
|---|---|
| Plataforma (9) contra controle complexo | **inconclusivo** |
| Plataforma sem o PL 2630 (8) contra controle complexo (**versão cega**) | **inconclusivo** |
| Subconjunto "conteúdo" (6) contra controle complexo | inconclusivo |
| Subconjunto "conteúdo" sem o PL 2630 (5) | compatível com complexidade |
| Plataforma contra controle geral | inconclusivo |

### Cada projeto de plataforma

| Projeto | Assunto | Urgência | Votação | Espera | Percentil no controle complexo (limite inferior) |
|---|---|---|---|---|---|
| PL 5587/2016 | Transporte por aplicativo | 4 abr. 2017 | no mesmo dia | 0 dias | 0 |
| PL 9348/2017 | Alerta Âmber em redes sociais | 14 jul. 2025 | 15 jul. 2025 | 1 dia | 0,13 |
| PL 3444/2023 | Influenciadores e provedores | 9 out. 2025 | 15 out. 2025 | 6 dias | 0,27 |
| PL 4709/2025 | Golpe do falso advogado (Marco Civil) | 12 nov. 2025 | 17 mar. 2026 | 125 dias | 0,67 |
| PL 1579/2025 | Alimentação de entregadores de aplicativo | 10 set. 2025 | — | 416+ dias | 0,74 |
| PL 2610/2025 | Responsabilidade de plataformas por indução a riscos | 21 ago. 2025 | — | 436+ dias | 0,74 |
| PL 130/2020 | Remoção de vídeos de infrações de trânsito | 16 jul. 2020 | 28 set. 2021 | 439 dias | 0,74 |
| PL 8889/2017 | Vídeo sob demanda | 16 ago. 2023 | 4 nov. 2025 | 811 dias | 0,76 |
| PL 2630/2020 | Lei das Fake News | 25 abr. 2023 | — | 1.285+ dias | 0,76 |

Medianas (Kaplan-Meier):

- plataforma: 439 dias;
- plataforma sem o PL 2630: 125 dias;
- controle complexo: **23 dias**;
- controle geral: 29 dias.

### Por que deu inconclusivo: um limite da régua, descoberto nos dados

- **Um em quatro projetos do controle nunca foi votado.** São 60 de 264 no controle complexo, ainda esperando depois de uma mediana de mais de três anos.
- **O teto da conta.** O percentil registrado é conservador: conta só os projetos do controle cuja espera foi observada. Por isso ele quase não passa de 0,77, por mais longa que seja a espera do projeto de plataforma.
- **O efeito.** Quatro projetos de plataforma com mais de um ano de espera ficaram em 0,74, a um passo de 0,75, e foram classificados como indeterminados.

A regra não foi mudada depois de vista. O limite fica registrado como lição para os próximos protocolos (desvio 8).

## Segunda linha da P2: o momento dos adiamentos

| Grupo | Adiamentos no plenário | Em janela eleitoral |
|---|---|---|
| Plataforma | 10 | **0** (0%) |
| Controle complexo | 174 | 10 (5,7%) |
| Controle geral | 483 | 48 (9,9%) |
| Esperado por acaso | | cerca de 1/6 |

- **Plataformas:** nenhum adiamento caiu perto de eleição. Esta linha **não é compatível com estratégia eleitoral**.
- **Todos os grupos:** ficam abaixo do acaso, provavelmente porque o plenário se reúne menos em período eleitoral. É uma leitura nossa, a conferir.

## Exploração fora do protocolo (rótulo: *post hoc*, não conta como teste)

A distribuição das esperas tem duas formas: ou o projeto é votado em dias, ou cai numa "gaveta" de mais de um ano. Daí a pergunta exploratória: que parte de cada grupo cai na gaveta, isto é, fica mais de um ano sem votação?

| Grupo | Na gaveta (> 365 dias) |
|---|---|
| Plataforma | 5 de 9 (56%) |
| Plataforma sem o PL 2630 | 4 de 8 (50%) |
| Controle complexo | 66 de 258 (26%) |
| Controle geral | 225 de 815 (28%) |

- **A diferença.** Teste exato de Fisher, unilateral: p = 0,06 com o PL 2630 e p = 0,13 sem ele. Com 9 projetos e uma análise escolhida depois de ver os dados, isso é **palha ao vento**, não evidência.
- **Leitura de Kaplan-Meier,** também exploratória: os quatro projetos parados há mais de um ano ficam por volta do percentil 75 do controle complexo, e não muito acima dele.

## Leitura (inferências nossas)

1. **A P2 não foi decidida.** O registrado diz inconclusivo, e a versão cega sem o PL 2630 também.
2. **A gaveta é a forma comum do atraso na Câmara, para qualquer tema.** Um em cada quatro projetos complexos com urgência aprovada nunca chega a voto. O PL 2630 é um caso extremo de um fenômeno geral, e não uma exceção.
3. **Plataforma não é um bloco.** Os projetos que tratam de serviços (transporte por aplicativo), de crianças (Alerta Âmber) ou de golpes passaram rápido ou em poucos meses. Os que tratam de responsabilidade e moderação de conteúdo (PL 2630, PL 2610) ou de trabalho em aplicativo (PL 1579) ficaram parados. É sugestivo, mas são poucos casos.
4. **Nenhum sinal de calendário eleitoral** nos adiamentos.

**Grau de certeza.**
- **Estabelecido:** as esperas e as contagens, com dados oficiais e o controle de qualidade (a) aprovado.
- **Em aberto:** se o atraso é estratégia.
- **Palha ao vento:** a maior chance de gaveta para os projetos de plataforma.

## O que poderia decidir a questão

- **Mais casos:** estender ao Senado, ou somar os projetos de plataforma que nunca tiveram urgência, comparados pelo tempo parado.
- **Uma nova previsão registrada,** com a régua da "gaveta" (mais de um ano sem voto) definida antes, aplicada a projetos com urgência aprovada **daqui para a frente**: por exemplo, os de IA (ver P3).
- **O controle de qualidade (b),** pendente.

## Arquivos

- **Dados brutos:** `dados/brutos/urgencias/` (votações, requerimentos, fichas e tramitações).
- **Processados:**
  - `dados/processados/urgencias_classificacao.csv`
  - `dados/processados/urgencias_esperas.csv`
  - `dados/processados/urgencias_resultado.json`
- **Scripts:**
  - `scripts/urgencias_coleta.py`
  - `scripts/urgencias_alvos.py`
  - `scripts/urgencias_classifica.py`
  - `scripts/urgencias_tramitacoes.py`
  - `scripts/urgencias_teste.py`
