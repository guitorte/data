# Instruções para o Claude neste repositório

Este é o repositório de pesquisa "A lei como preço", de Guilherme. Ele estuda o que acontece quando um Estado aplica a própria lei a uma plataforma digital global e a disputa escala para o comércio e as sanções entre países. O caso central é Brasil × X e Rumble (2024–2026).

## Antes de qualquer coisa

1. Leia `docs/estado-atual.md`. É a passagem de turno: onde paramos, o que está pendente, o que foi decidido.
2. Se a tarefa for pesquisa, releia `standards.txt`. Ele é obrigatório: o usuário pediu que toda pesquisa siga esse arquivo.
3. Não reabra decisões registradas em `docs/decisoes.md` sem motivo novo. Se houver motivo, diga qual.

## Idioma e estilo

- Responda em português, que é o idioma do projeto até aqui.
- Se a mensagem do usuário começar ou terminar com "usen", passe a responder em inglês a partir dali; com "br", volte ao português. Se a mensagem for só "usen" ou "br", repita a resposta anterior no idioma pedido.
- Escreva para leitura fluente: frases claras, ideias abstratas ancoradas em exemplos concretos ou metáforas. O projeto já tem um vocabulário próprio de imagens (pedágio, taxímetro, guincho, motor e veículo, escada da intenção); use-o com parcimônia nas seções de método e resultados.
- Se o usuário estiver apressando ou pressionando, diga isso com franqueza e proponha um processo melhor.

## Regras de pesquisa (resumo do `standards.txt` e dos hábitos do projeto)

- **Cite só o que foi lido nesta sessão.** Nunca reconstrua referência, citação, página ou URL de memória. Se lembrar de algo sem ter lido, escreva "de memória, conferir" e trate como pista, não como fonte.
- **Fonte primária primeiro.** Para dados e estatísticas, vá ao órgão que produziu o número. Se não conseguir, avise.
- **Citações exatas,** com cortes marcados. Paráfrase sem esticar o que a fonte diz.
- **Atribua opiniões** ("segundo X") e marque como **inferência nossa** toda conclusão que nenhuma fonte afirma sozinha.
- **Marque o grau de certeza** com as etiquetas do projeto: **estabelecido** (documento primário), **sustentado** (bons indícios), **contestado** (fontes boas em conflito; apresente os dois lados), **em aberto**.
- **Corroboração independente:** cinco veículos repetindo um comunicado são uma fonte só.
- **Equilíbrio é pesar, não contar lados.** Evite tanto o falso equilíbrio quanto a falsa assimetria. "Os dois lados fazem X" não é "fazem X na mesma medida": a segunda frase precisa de dados.
- **"Lawfare" e "censura" são objetos de estudo, não categorias de análise.** A pesquisa registra quem usa o rótulo, contra quem, quando e com que efeito; não decide se o rótulo é verdadeiro.
- **Teste do espelho:** um mecanismo proposto precisa explicar os usos de todos os lados, ou de nenhum.
- **Busque evidência contra a tese,** não só a favor. Quando surgir uma explicação mais simples, não reinterprete a hipótese para caber nela; escreva o que precisaria ser verdade para a hipótese ainda valer e vá checar só isso.

## Como dividir o trabalho

Antes de começar uma tarefa com mais de um passo, divida-a em etapas e recomende um nível de esforço para cada uma. Espere o usuário confirmar ou alterar antes de prosseguir. O objetivo é economizar onde o trabalho é mecânico e gastar onde um erro se propaga.

- **Baixo:** execução com caminho conhecido, como rodar um script já escrito, baixar dados de uma API testada ou registrar e fazer commit.
- **Médio:** código novo ou análise com poucas decisões de julgamento.
- **Alto:** decisões de desenho (protocolo, definições, seleção de casos), interpretação de evidência e textos que entram nos achados ou na tese.
- **Máximo:** só para decisões que mudam o rumo do trabalho, como a escolha da pergunta no ponto de controle.

Para economizar: scripts gravam os resultados em arquivo e mostram só resumos; nada de despejar JSON grande na conversa.

## Como registrar o trabalho

Toda expedição de pesquisa deixa três rastros:

1. **Os dados:** o que veio de uma API ou download vai para `dados/brutos/` e nunca é editado à mão. O que for calculado sai de um script em `scripts/` e vai para `dados/processados/`. Registre a data da coleta.
2. **As fontes:** cada base, dossiê ou documento novo tem uma seção "Fontes e consultas" com URL, data e o que foi consultado. Documentos baixados entram em `fontes/` e numa linha de `fontes/catalogo.md`.
3. **O texto:** os achados vão para o arquivo da base ou do dossiê. O resumo, com o grau de certeza, vai para `docs/achados.md`. Mudanças de tese vão para `docs/tese-e-hipoteses.md`; decisões, para `docs/decisoes.md`; previsões feitas antes dos dados, para `docs/previsoes.md`.

Ao encerrar uma sessão, atualize `docs/estado-atual.md` (data, o que mudou, próximos passos) e proponha um commit.

## Material de entrada (`entrada/`)

O usuário traz material de fora por `entrada/novos/`. Também pode pedir que você importe uma conversa dele com o Claude; nesse caso, use as ferramentas de busca e leitura de conversas e importe só o que ele pedir. Instruções para o usuário estão em `entrada/LEIAME.md`.

No começo da sessão, ou quando o usuário pedir, veja se há arquivos em `entrada/novos/` além do LEIAME. Se houver, avise e proponha a triagem (esforço médio). Para cada item:

1. **Direitos e privacidade.** O repositório é público. Se o item tiver texto integral protegido por direito autoral ou dados pessoais, avise o usuário antes de qualquer coisa. Apagar o arquivo não o tira do histórico do Git; diga isso.
2. **Classificação:** primária, pesquisa, nota ou terceiros. Tudo o que vem de outras conversas é **pista**, não fonte. As referências que ele cita precisam ser abertas e lidas antes de virar achado.
3. **Registro:** uma linha em `entrada/triagem.md`.
4. **Destino:**
   - fontes primárias públicas vão para `fontes/` e para o catálogo;
   - pistas vão para os candidatos da base ou do dossiê;
   - suspeitas novas vão para `docs/tese-e-hipoteses.md`.

   Nada vai direto para `docs/achados.md`.
5. **Arquivo:** mova o original com `git mv` para `entrada/triados/`, sem editá-lo.
6. **Commit.** A conferência das afirmações é outra etapa (esforço alto) e só acontece com a confirmação do usuário.

## Direitos autorais

- **Livros não entram no repositório.** Eles ficam na pasta "Pdfs" do Google Drive do usuário (lista em `fontes/livros.md`). Se precisar deles, use o conector do Google Drive ou peça ao usuário. Uma pasta local `livros/` está no `.gitignore` para uso temporário.
- Do texto de livros, use só citações curtas, e prefira paráfrase.
- Documentos de terceiros com direitos (por exemplo, os comentários da CCIA) entram no catálogo só como link.
- Documentos do governo americano são de domínio público e podem ficar em `fontes/primarias-eua/`.

## Acesso à rede (o que já se sabe)

- Respondem por `curl`: ustr.gov, govinfo.gov, lda.gov, as APIs de dados abertos do Senado (`legis.senado.leg.br/dadosabertos`) e da Câmara (`dadosabertos.camara.leg.br/api/v2`).
- O Senado devolve JSON com o cabeçalho `Accept: application/json`. Discursos em plenário só existem a partir de mar. 2017.
- `comments.ustr.gov` bloqueia leitura automatizada: os comentários escritos da Seção 301 precisam ser baixados à mão pelo usuário.
- Para o *Federal Register*, use os PDFs do govinfo (`govinfo.gov/content/pkg/FR-AAAA-MM-DD/pdf/...`).
- Esses acessos dependem do ambiente em que o Claude Code roda; confira antes de prometer.

## Convenções

- Commits pequenos, com mensagem em português que diga o que mudou e por quê.
- Scripts em Python 3, só com a biblioteca padrão, rodados da raiz do repositório (`python3 scripts/<nome>.py`).
- Datas no formato "2 nov. 2026" nos textos e AAAA-MM-DD em nomes de arquivo e dados.
- O manuscrito (`manuscrito/`) está parado. Não edite o rascunho sem pedido explícito: a seção 2 só deve ser reescrita depois que o usuário escolher a pergunta do trabalho.
