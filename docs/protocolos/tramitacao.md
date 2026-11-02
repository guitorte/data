# Protocolo · Expedição da tramitação (previsão P2)

**Versão 1, 2 nov. 2026. Status: aprovado pelo usuário em 2 nov. 2026 (12h14), antes de abrir qualquer dado de tramitação.** Depois de aprovado, este protocolo não se edita. Mudanças viram desvios datados, no fim do arquivo, com o motivo.

## 1. Para que serve

A previsão P2 (`docs/previsoes.md`) pergunta se o atraso na regulação de plataformas é **estratégia** ou **complexidade**. Este protocolo fixa, antes de abrir os dados, o que vamos medir, contra o quê, e que resultado conta para cada lado. A ideia é amarrar as mãos antes de ver as cartas: se a régua for escolhida depois, qualquer resultado pode ser lido a favor da tese.

## 2. O que já sabemos antes dos dados (declaração de conhecimento prévio)

O PL 2630 **não é um caso cego.** Antes de abrir qualquer dado, a conversa e a memória já continham estas afirmações. Todas são de memória e ainda precisam ser conferidas:

- o PL 2630/2020 nasceu e foi aprovado no Senado em 2020;
- Google e Telegram fizeram campanha contra ele em 2023;
- ele "morreu" na Câmara;
- o STF julgou o artigo 19 do Marco Civil em jun. 2025;
- (acrescentado em 2 nov. 2026, ainda antes da aprovação e dos dados) uma conversa importada informa que, em maio de 2023, a Senacon usou o Código de Defesa do Consumidor contra o link do Google que atacava o PL 2630, e que a regra sobre plataformas veio depois por decreto (12.975/2026) e pela tese do STF, "até o Congresso aprovar nova lei".

Por isso, o PL 2630 entra como **estudo de caso**, que ilustra e descreve. O **teste** da P2 é a comparação da seção 4, em que não conhecemos o resultado dos outros projetos. Os resultados serão apresentados com e sem o PL 2630. A versão sem ele é a cega.

Consultas feitas antes deste registro, nenhuma com dados do PL 2630:

- a tabela de tipos de tramitação da Câmara (235 códigos), salva em `dados/brutos/camara/referencia_tipos_tramitacao_2026-11-02.json`;
- um teste do serviço de votações do plenário em ago. 2019, que mostrou 10 votações ligadas a urgência no mês, com o requerimento como objeto;
- dois testes de busca por palavra-chave.

## 3. Definições

### 3.1 Eventos de tramitação (Câmara)

A tabela de códigos da Câmara foi classificada **antes** dos dados, em três grupos.

**Grupo A, andamento deliberativo:** passos formais rumo a uma decisão, ou a própria decisão.

- **Pauta:** 150, 151, 1058.
- **Urgência:** 196, 215.
- **Pareceres:** 210, 214, 322 a 326, 330, 335 a 340, 1027 a 1030, 1040.
- **Discussão e votação:** 216, 219, 220, 222, 227, 231 a 233, 237 a 240, 244, 245, 1231, 1233, 1235 a 1240, 1500.
- **Comissões temporárias e especiais:** 120, 121, 122, 1071.
- **Desfechos:** 128, 137, 197, 198, 200, 251, 469, 502, 608, 609, 1012, 1013, 1024, 1025, 1241, 1518, 1519.

**Grupo B, adiamento ou obstáculo:**

- 221 (adiamento de discussão);
- 234 (adiamento de votação);
- 250 (retirada de pauta);
- 1008 (não deliberado);
- 223 e 1232 (obstrução);
- 420 (pedido de vista);
- 1038 (volta a aguardar comissão especial).

**Grupo C, administrativo:** todos os demais. São recebimentos, publicações, notificações, encaminhamentos, prazos, requerimentos genéricos, apensações e designações de relator.

Designar relator fica no grupo C de propósito. É um passo barato, que pode acontecer sem que o projeto ande, e contá-lo como andamento faria um projeto engavetado parecer vivo.

### 3.2 Medidas

- **Espera na urgência (medida principal):** dias entre a aprovação da urgência no plenário (código 196 ou votação equivalente) e a primeira deliberação de mérito no plenário. Contam como deliberação os códigos 1235, 1236, 244, 197, 1500, 128, 608 e 609, o primeiro que ocorrer. Sem deliberação até 31 out. 2026, o caso é **censurado**: sabemos só que a espera foi de pelo menos aquele tempo.
- **Tempo parado (secundária):** soma dos intervalos de **180 dias ou mais** entre eventos dos grupos A ou B, dividida pela vida do projeto na Câmara. A vida vai da chegada à Câmara ao desfecho, ou até 31 out. 2026. Como verificação de robustez, a mesma medida é calculada descontando os recessos constitucionais (18 a 31 jul. e 23 dez. a 1º fev.; datas de memória, conferir no art. 57 da Constituição na etapa 2.2).
- **Adiamentos (secundária):** número de eventos do grupo B no plenário e data de cada um.

### 3.3 Janela eleitoral

Vai de 90 dias antes do primeiro turno até o segundo turno, nas eleições gerais e municipais de 2016 a 2026. As datas vêm do TSE na etapa 2.2. A janela cobre cerca de um sexto do calendário, porque há eleição em todo ano par. Essa é a taxa esperada por acaso.

### 3.4 Projeto sobre plataformas (regra P)

Um PL é "sobre plataformas" quando passa nos dois filtros:

1. **Termos.** A ementa ou a indexação menciona pelo menos um destes termos:
   - "plataforma(s) digital(is)", "rede(s) social(is)", "provedor(es) de aplicação/aplicações", "aplicações de internet";
   - "serviço(s) de mensageria" ou "mensagem instantânea";
   - "ferramenta(s) de busca", "buscador(es)";
   - "Marco Civil da Internet" ou "Lei nº 12.965";
   - "desinformação", "notícias falsas" ou "fake news";
   - "moderação de conteúdo", "conteúdo(s) gerado(s) por terceiros".
2. **Leitura da ementa.** O projeto impõe deveres, responsabilidade ou sanções **às plataformas ou provedores**.

Ficam fora:

- projetos que só tipificam crime de pessoas pela internet;
- projetos que só usam a internet como meio (ensino a distância, por exemplo);
- proteção de dados pessoais e tributação, que são outros debates.

**Como evitar contaminação:** a classificação é feita só com ementa e indexação, salva e registrada no Git **antes** de ligar os projetos às suas esperas. Os casos de fronteira vão para uma lista com a justificativa de cada decisão.

### 3.5 Grupo de controle complexo (regra C)

Os projetos que não são de plataformas e cuja ementa contém "marco legal", "código", "estatuto", "lei geral", "política nacional" ou "sistema nacional". A ideia é comparar com leis de arquitetura parecida, e não com homenagens e datas comemorativas. O controle geral é formado por todos os demais projetos com urgência aprovada.

## 4. O teste da P2 (comparativo, cego para os demais projetos)

**População.** Os PLs com urgência (arts. 154 ou 155 do Regimento) aprovada no plenário da Câmara entre 1º fev. 2015 e 30 abr. 2026. O corte de abril deixa ao menos seis meses de observação. A urgência pedida pelo presidente (art. 64 da Constituição) fica fora, porque é outro mecanismo.

**Fonte.** O serviço de votações do plenário (`/votacoes?idOrgao=180`), mês a mês, com descrição de urgência aprovada. Do requerimento chega-se ao PL pela ementa ("Requer [...] urgência para o PL nº ...").

**Controle de qualidade:**

- conferir, numa amostra de 20 PLs, que a tramitação de cada um tem o código 196 na data;
- conferir que os projetos da regra P que aparecem em busca por palavra-chave com código 196 estão na população. Se faltar algum, a coleta tem vazamento, e isso será registrado.

**Escala.** Para cada projeto de plataforma, calcula-se o percentil da sua espera dentro do controle complexo. O cálculo trata os censurados como "pelo menos" a espera observada, com a mediana pelo estimador de Kaplan-Meier.

**Regra de decisão:**

| Resultado | Leitura |
|---|---|
| Mais da metade dos projetos de plataforma acima do percentil 75 do controle complexo | **Compatível com estratégia** |
| Mais da metade no percentil 75 ou abaixo | **Compatível com complexidade** (não há atraso especial) |
| Menos de 3 projetos de plataforma na população | **Sem força de teste.** Os percentis são relatados um a um, e o resultado vale no máximo como "palha ao vento" |

O mesmo é relatado contra o controle geral, para mostrar quanto a complexidade explica.

**Segunda linha da P2 (o momento dos adiamentos).** Compara-se a parcela dos adiamentos do grupo B que cai em janela eleitoral entre os projetos de plataforma e os de controle. A taxa esperada por acaso é de cerca de um sexto. Se a parcela das plataformas for maior que a do controle, a linha é compatível com estratégia.

## 5. O estudo de caso do PL 2630 (descritivo)

- **Linha do tempo nas duas Casas.** No Senado, a tramitação vem pelo serviço de dados abertos; na Câmara, pelos códigos da seção 3.1. Inclui tempo parado, adiamentos e urgências.
- **Contexto de cada adiamento relevante.** Contam como relevantes:
  - os eventos do grupo B no plenário;
  - as urgências não votadas em 30 dias.

  Se passarem de dez, ficam os dez seguidos dos maiores intervalos parados. Para cada um, registra-se se nos 30 dias anteriores houve:
  - **campanha de plataforma:** ação pública assinada pela empresa sobre o projeto (blog, aviso no aplicativo, anúncio, nota oficial), ou relatada por pelo menos dois veículos independentes;
  - **janela eleitoral;**
  - **crise:** decisão judicial contra plataforma, episódio de violência ou similar, com data;
  - **divergência de mérito documentada:** mudança de texto pelo relator, orientação de bancada contrária, requerimento que justifique o adiamento pelo conteúdo;
  - **motivo declarado** no próprio registro ou requerimento, transcrito.
- **Leitura de cada adiamento:**
  - campanha ou janela sem divergência de mérito: padrão de estratégia;
  - divergência de mérito sem campanha: padrão de complexidade;
  - as duas juntas: **misto**. É o resultado mais provável, porque campanhas costumam argumentar o mérito, e ele não conta para nenhum lado.
- **Janela de omissão.** São os dias entre o último evento do grupo A do PL 2630 na Câmara e o julgamento do artigo 19 do Marco Civil pelo STF, com a data conferida no site do STF.
- **Quem ganha com o relógio.** Conta-se quantos eventos da Base 1 (ordens contra plataformas) caem dentro e fora dos períodos parados do PL 2630. É só descrição, sem teste.

## 6. Fontes e cuidados

- Dados da Câmara e do Senado: serviços oficiais de dados abertos. As datas das eleições vêm do TSE.
- Para o contexto dos adiamentos, primeiro as fontes primárias: notas taquigráficas, Agência Câmara, comunicados das próprias empresas. Depois, imprensa independente com data. Fato contestado precisa de duas origens separadas.
- Tudo segue o `standards.txt`, com as etiquetas estabelecido, sustentado, contestado e em aberto.

## 7. Limites conhecidos de antemão

- **Projetos de plataforma com urgência aprovada devem ser poucos,** e o teste pode terminar sem força. Saber disso antes é parte do protocolo; não é motivo para trocar a régua depois.
- **A urgência é um filtro de saliência.** Ela compara projetos que a Câmara disse querer votar logo, e não todos os projetos, a maioria dos quais morre na gaveta por qualquer motivo.
- **A regra C mede complexidade pelo nome da lei.** É um indicador grosseiro.
- **A Câmara foi escolhida para o teste** porque os dois grupos são medidos na mesma Casa, o que neutraliza a lentidão própria dela. Sabemos de antemão que o PL 2630 parou lá, e por isso a versão sem ele é a que conta.

## 8. Desvios

Cada desvio entra aqui com data, o que mudou e por quê.

1. **2 nov. 2026, etapa 2.3 — o despacho prevalece sobre o código.** No PL 2630, o evento de 2 maio 2023 tem o código 1241 ("Retirada pelo Autor(a)"), mas o despacho diz "Retirado de pauta, de ofício". Regra adotada para todos os projetos: quando o despacho diz "retirado de pauta", o evento conta como grupo B. Motivo: o código contradiz o texto do próprio registro. A regra foi fixada depois de ver o PL 2630, que não é cego, e antes de abrir os demais projetos.
2. **2 nov. 2026, etapa 2.2 — datas eleitorais.** O protocolo previa tirar as datas do TSE. O site do TSE e o do Planalto bloquearam o acesso automatizado. A data de 2020 veio da Agência Senado; as outras seguem a regra constitucional, marcadas como "a conferir" em `dados/referencia/calendario_eleitoral.csv`.
3. **2 nov. 2026, limitação observada (sem mudança de regra).** A tramitação da Câmara não registra a inclusão em pauta (código 150) do PL 2630, embora ele tenha sido retirado de pauta. Na etapa 2.5, os adiamentos e as votações devem ser buscados também no serviço de votações do plenário, como o protocolo já prevê para a urgência.
4. **2 nov. 2026, etapa 2.5 — correção de coleta.** A primeira versão do script só reconhecia o PL alvo no formato "PL 123/2020" e perdia "Projeto de Lei nº 1.234, de 2020". O controle de qualidade pegou a falha antes de qualquer desfecho ser aberto. Com a correção (`scripts/urgencias_alvos.py`), 1.147 dos 1.478 requerimentos foram ligados a um PL. Os 331 restantes tratam de outros tipos de proposição (PLP, PDL, projetos de resolução, mensagens) ou têm ementa sem alvo identificável.
5. **2 nov. 2026, etapa 2.5 — subconjunto declarado antes dos desfechos.** Aplicada ao pé da letra, a regra P também inclui projetos que impõem deveres a plataformas fora da disputa sobre conteúdo: trabalho em aplicativos de entrega, transporte por aplicativo, vídeo sob demanda. A **regra P literal continua sendo a medida principal**, porque foi a aprovada. Fica declarado agora, antes de abrir qualquer espera, um **subconjunto secundário "P-conteúdo"**: deveres sobre o conteúdo que circula na plataforma (remoção, moderação, publicidade, difusão obrigatória). As decisões, projeto a projeto, com a justificativa de cada uma, estão em `dados/referencia/urgencias_decisoes_P.csv`.
6. **2 nov. 2026, etapa 2.5 — fichas não encontradas.** 30 dos 1.153 PLs alvo não tiveram a ficha encontrada pela busca por número e ano. Ficam como "sem_ficha", fora dos três grupos, e entram como limite. Quantos são de plataforma não se sabe.
7. **2 nov. 2026, etapa 2.6 — detalhes de cálculo fixados antes de baixar os desfechos.**
   - **Data da urgência:** a primeira aprovação de urgência no plenário para o PL dentro do período (votação do requerimento).
   - **Fonte da deliberação:** a tramitação de cada PL na Câmara, com os códigos da seção 3.2, considerando a primeira ocorrência na data da urgência ou depois. Valem também os "despachos prevalecem" (desvio 1).
   - **Censura:** se não houver deliberação até 31 out. 2026, a espera é censurada nessa data.
   - **Percentil:** o de cada projeto de plataforma é calculado contra o controle complexo pelo limite inferior, isto é, a fração dos projetos do controle com espera observada (não censurada) menor que a dele. Isso aplica o "pelo menos" do protocolo e é conservador para a leitura de estratégia. O limite superior também é relatado.
   - **Mediana:** a de cada grupo, pelo estimador de Kaplan-Meier.
   - **Controle de qualidade (a):** amostra aleatória de 20 PLs (semente fixa 2026) para conferir se o código 196 aparece na tramitação até 7 dias depois da data da votação.
8. **2 nov. 2026, depois do resultado — limite da régua e análises exploratórias.** Um em cada quatro projetos do controle complexo nunca foi votado (60 de 264). Por isso o percentil conservador (limite inferior) fica abaixo de cerca de 0,77 mesmo para esperas muito longas, e o critério "acima do P75" ficou quase inalcançável. A regra **não** foi mudada: o resultado registrado é "inconclusivo". As análises da "gaveta" (mais de um ano sem voto) e do percentil por Kaplan-Meier foram feitas **depois** de ver os dados e estão rotuladas como exploratórias em `dossies/tramitacao-teste-p2.md`. Lição para os próximos protocolos: definir o percentil por Kaplan-Meier, ou fixar de antemão uma régua de "gaveta". O controle de qualidade (b) não foi feito.

