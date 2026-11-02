# Entrada: como trazer material novo

Esta pasta é a caixa de entrada do projeto. Tudo que chega de fora (pesquisas feitas em outras conversas, documentos, notas suas) entra aqui primeiro. Depois o Claude faz a triagem e decide para onde cada coisa vai.

Funciona como a bancada de recebimento de um laboratório: nada vai direto para a prateleira. Primeiro se confere o que é, de onde veio e se está em condições de uso.

## Antes de subir: o repositório é público

Qualquer pessoa pode ler o que estiver aqui, e o histórico do Git guarda até o que for apagado depois. Por isso:

| Pode subir aqui | Não suba aqui |
|---|---|
| Respostas e pesquisas de outras conversas com o Claude | Livros, artigos pagos e relatórios com direitos autorais completos |
| Suas notas e rascunhos | Documentos pessoais ou de terceiros com dados privados |
| Documentos públicos de governo, tribunais, Congresso | Material que você não quer tornar público |
| Links, listas de fontes, transcrições de fala pública | |

O que não pode vir para cá vai para o Google Drive, na pasta "Pdfs" ou numa pasta nova. Depois é só me avisar: eu leio pelo conector e trago para o repositório só a ficha, o resumo e o link.

## Quatro jeitos de trazer material, do mais fácil ao mais trabalhoso

1. **Pesquisa de outra conversa com o Claude:** diga o título da conversa ou cole o link (`claude.ai/chat/...`). Eu consigo ler suas outras conversas e trago para cá só o que você pedir.
2. **Arquivo no celular:** anexe na conversa com o Claude. Eu salvo aqui com o nome certo.
3. **Texto colado, direto no GitHub:**
   - abra a pasta `entrada/novos/` no navegador e toque em *Add file* → *Create new file*;
   - dê o nome `AAAA-MM-DD_origem_assunto.md`, por exemplo `2026-11-02_chat_decretos-marco-civil.md`;
   - cole o texto e, se quiser, o cabeçalho de `entrada/modelo.md`;
   - toque em *Commit changes*.
4. **Arquivo, direto no GitHub:** abra `entrada/novos/` e toque em *Add file* → *Upload files*. Se a opção não aparecer no celular, ative a versão para computador do navegador.

O cabeçalho do modelo é opcional, mas ajuda: origem, data, o que é e por que pode ser útil. Sem ele, eu deduzo pelo conteúdo e pergunto o que faltar.

## O que acontece depois

Quando houver material em `entrada/novos/`, peça "faça a triagem da entrada". Para cada item, eu:

1. leio e confiro se pode ficar num repositório público;
2. classifico: fonte primária, pesquisa de outra conversa, nota sua ou documento de terceiros;
3. registro em `entrada/triagem.md` o que é, para que serve e para onde foi;
4. levo o que interessa para o lugar certo:
   - fontes primárias públicas vão para `fontes/` e para o catálogo;
   - pistas vão para a lista de candidatos da base ou do dossiê correspondente;
   - ideias novas vão para `docs/tese-e-hipoteses.md`, marcadas como suspeita;
5. movo o original para `entrada/triados/`, onde ele fica guardado sem alteração.

## Uma regra importante

O que chega de outras conversas entra como **pista, não como fonte**. Uma resposta de pesquisa é como o fichamento de um colega: ajuda a achar o livro, mas não substitui lê-lo. Cada afirmação só vira achado depois que a fonte original for aberta e lida numa sessão, como manda o `standards.txt`.

## Esforço

- **Triagem: médio.** É leitura e classificação.
- **Conferir as afirmações nas fontes originais: alto.** É feito à parte, só para o que importar, e com a sua confirmação.
