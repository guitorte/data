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

## Etapa 2.4: o que cercou cada momento (2 nov. 2026)

As categorias são as do protocolo, sempre nos 30 dias anteriores ao evento. Uma ausência quer dizer "não encontrada nas fontes lidas", e não que a coisa não existiu.

### O grupo de trabalho de 2021 (correção ao "parado")

- **O que houve:** Arthur Lira instituiu um grupo de trabalho para o PL 2630 em junho de 2021, com prazo de 90 dias prorrogáveis e Orlando Silva como relator [T1]. O grupo aprovou o relatório-base em 1º dez. 2021 [T2].
- **Grau de certeza:** **sustentado**, por dois textos do mesmo veículo especializado.
- **Por que não aparece na medida:** esse trabalho não está na tramitação do projeto, por isso a medida do protocolo não o vê.
- **Correção:** contando o grupo de trabalho e a votação de abr. 2022 como andamento, a fração do tempo parado cai de 99,7% para cerca de **87%**. É uma conta de robustez, com datas aproximadas, e não uma mudança de regra.

### 6 abr. 2022: urgência rejeitada

- **Votação:** 249 votos a favor, 207 contra; eram necessários 257 [C1].
- **Campanha de plataforma:** não encontrada nas fontes lidas.
- **Janela eleitoral:** não. A janela do protocolo só começa em 4 jul. 2022, embora fosse ano de eleição.
- **Crise:** não encontrada nas fontes lidas.
- **Divergência de mérito documentada:** sim [C1].
  - Marcel van Hattem (Novo) falou em limite à liberdade de expressão e chamou de "soviética" a análise de conteúdo proposta.
  - Giovani Cherini (PL) disse que o projeto buscava inviabilizar "o projeto eleitoral do governo Bolsonaro".
  - Daniel Silveira (PTB), réu no STF, disse que o texto "será usado para prejudicar qualquer tipo de oponente político".
- **Motivo declarado:** insuficiência de votos. O relator respondeu que o Parlamento não podia se omitir e deixar o Judiciário definir as regras [C1].
- **Leitura pelo protocolo:** padrão de **complexidade**, isto é, divergência de mérito sem campanha. Ressalva nossa: parte da divergência é disputa eleitoral, não técnica. Uma reportagem diz que a rejeição teve apoio do governo Bolsonaro, mas não a lemos; fica como pista.

### 25 abr. 2023: urgência aprovada

- **Votação e manobra:** 238 a 192. Segundo o Aos Fatos, a aprovação "só se concretizou por uma manobra regimental do presidente da Câmara, Arthur Lira" [A1].
- **Por que não é codificada:** a urgência é o começo da espera, não um adiamento. Fica como contexto.

### 2 maio 2023: retirada de pauta

- **Campanha de plataforma:** **sim**, segundo o Aos Fatos [A1]:
  - o Google exibiu um link contra o projeto, sem identificação, retirado depois de notificação da Senacon;
  - as mensagens da Meta usaram argumentos distorcidos;
  - os anúncios políticos contra o projeto no Facebook e no Instagram quintuplicaram.
- **Janela eleitoral:** não.
- **Crise:** não codificada; nenhuma foi encontrada nas fontes lidas.
- **Divergência de mérito documentada:** **sim** [A1][T3].
  - A Frente Parlamentar Evangélica orientou voto contra, depois de circular a alegação falsa de que o projeto censuraria versículos da Bíblia.
  - O relator retirou o órgão regulador.
  - O Republicanos passou a se opor ao mérito.
- **Motivo declarado** [T3]:
  - o relator pediu tempo para "adaptar o relatório às novas contribuições que diversas bancadas fizeram";
  - Lira lembrou que a escolha da pauta é prerrogativa dele, ouviu os líderes e retirou o projeto, sem marcar nova data;
  - Sóstenes Cavalcante (PL) disse que já se sabia que o projeto não passaria.
- **Leitura pelo protocolo:** **misto**, campanha e divergência de mérito ao mesmo tempo. Era o resultado previsto, e ele não conta para nenhum lado.

### Depois da retirada (fora da janela, registrado para contexto)

- **Telegram, 9 maio 2023:** mensagem contra o projeto disparada a todos os usuários (várias reportagens; não lidas aqui).
- **STF, 12 maio 2023 (Inq. 4.933):** a pedido da PGR, a partir de notícia-crime da Câmara assinada por Lira, Moraes abriu inquérito contra diretores do Google e do Telegram no Brasil pela "campanha abusiva" contra o PL 2630 [D1].
  - **Quem descreve a campanha:** a PGR usou "sórdida campanha de desinformação, manipulação e intimidação". A expressão é da PGR, citada na decisão; não é achado do tribunal.
  - **Grau de certeza: estabelecido** (documento primário).
  - **Por que importa:** é o tribunal entrando numa briga que estava no Legislativo, a pedido do próprio presidente da Câmara.

### O que a etapa 2.4 mostra (inferências nossas)

1. **O caso não decide a P2,** como previsto. Um momento tem padrão de complexidade (2022), o outro é misto (2023).
2. **O porteiro aparece por inteiro em 2023.** O mesmo presidente da Câmara cria o grupo de trabalho, aprova a urgência por manobra, retira o projeto da pauta invocando a própria prerrogativa e leva a campanha das plataformas ao STF. A demora passou por uma pessoa. Se foi estratégia dela, das plataformas ou cálculo de votos, o caso não permite dizer.
3. **A ponte com o tribunal é documentada.** Uma semana depois da retirada, a disputa legislativa virou inquérito no STF. É um exemplo concreto da suspeita 12: o tribunal como lugar para onde a briga escorre quando o Congresso trava.

### Fontes da etapa 2.4 (acesso em 2 nov. 2026)

- [C1] Agência Câmara. "Deputados rejeitam urgência a projeto de combate a fake news". 6 abr. 2022. <https://www.camara.leg.br/noticias/864946-deputados-rejeitam-urgencia-a-projeto-de-combate-a-fake-news/>
- [A1] Rudnitzki, Ethel; Lobato, Gisele. "O que levou o 'PL das Fake News' a perder apoio no Congresso". *Aos Fatos*, 5 maio 2023. <https://www.aosfatos.org/noticias/pl-das-fake-news-apoio-congresso/>
- [T1] Urupá, Marcos. "PL das Fake News será debatido em grupo de trabalho; Orlando Silva será relator". *Teletime*, 28 jun. 2021. <https://teletime.com.br/28/06/2021/pl-das-fake-news-sera-debatido-em-grupo-de-trabalho-orlando-silva-sera-relator/>
- [T2] Urupá, Marcos. "Texto-base do relatório do PL das Fake News é aprovado com complementação de voto". *Teletime*, 1º dez. 2021. <https://teletime.com.br/01/12/2021/texto-base-do-relatorio-do-pl-das-fake-news-e-aprovado-com-complementacao-de-voto/>
- [T3] Urupá, Marcos. "PL das Fake News tem votação adiada". *Teletime*, 2 maio 2023. <https://teletime.com.br/02/05/2023/pl-das-fake-news-tem-votacao-adiada/>
- [D1] STF. Inquérito 4.933/DF, decisão de 12 maio 2023, rel. Min. Alexandre de Moraes (cópia hospedada pelo Poder360). <https://static.poder360.com.br/2023/05/Decisao-Inquerito-4933.pdf>
- **Não abertas:**
  - Agência Brasil sobre a Senacon e o Google (2 maio 2023), fora da lista de acesso;
  - Poder360 sobre o adiamento, com erro no site.
