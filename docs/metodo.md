# Método

O método do projeto cabe numa frase: ler juntos documentos que disciplinas diferentes leem separados, e dizer antes o que derrubaria cada hipótese. A versão para o artigo está na seção 7 de `manuscrito/rascunho-artigo.md`. Este arquivo é a versão de bancada: regras, medidas e cuidados.

## 1. Graus de certeza

Todo achado leva uma etiqueta.

| Etiqueta | Quando usar |
|---|---|
| **Estabelecido** | Documento primário diz isso diretamente. |
| **Sustentado** | Bons indícios, de fontes independentes, sem documento decisivo. |
| **Contestado** | Fontes boas discordam. Apresente as versões e atribua cada uma; não escolha em silêncio nem tire a média. |
| **Em aberto** | Ainda não há evidência suficiente. Diga o que a resolveria. |

Duas marcas complementares:

- **inferência nossa**, para conclusões que nenhuma fonte afirma sozinha;
- **de memória, conferir**, para o que foi lembrado e não lido. Nada com essa marca entra no texto do artigo.

## 2. Testes de evidência (Collier)

David Collier classifica as evidências por necessidade e suficiência.

| Teste | Lógica | Imagem |
|---|---|---|
| **Aro** (*hoop*) | Necessário, não suficiente: a hipótese precisa passar para continuar viva, mas passar não a confirma. | O suspeito precisa estar na cidade no dia do crime. |
| **Arma fumegante** (*smoking gun*) | Suficiente, não necessária: confirma se aparecer, e a ausência não derruba. | A arma na mão do suspeito. |
| **Palha ao vento** (*straw in the wind*) | Nem necessária nem suficiente: só desloca um pouco a confiança. | Um boato de que o suspeito andava nervoso. |
| **Duplamente decisivo** | Necessário e suficiente. Raro. | Vídeo nítido do crime. |

Exemplo do projeto: em 2026, a hipótese rival (o aliado como motor) **falhou no aro**. Flávio Bolsonaro pediu na audiência que não houvesse tarifa, e ela veio oito dias depois.

## 3. A escada da intenção

A tese não depende de um plano secreto. Entre o "mal sem projeto" de Arendt e a conspiração há degraus, e cada um exige evidência diferente:

1. **Incentivo.** Alguém ganha com o resultado. Basta mostrar a exposição: o preço de uma ação, um contrato.
2. **Risco assumido.** O ator sabe do efeito provável e segue em frente; é o que o direito penal chama de dolo eventual.
3. **Estratégia declarada.** O ator diz o que pretende, em público.
4. **Coordenação aberta.** Os atores combinam publicamente.
5. **Plano secreto.** Exige documento interno ou testemunho.

**Regra.** Cada afirmação diz em que degrau está e não sobe sem evidência do degrau seguinte. Quase tudo o que a pesquisa achou está nos degraus 1 a 3, e em documentos públicos.

## 4. Como montar uma base

- **Uma linha por evento,** com campos fixos definidos antes da coleta. Uma planilha serve a muitas perguntas: se cada linha tiver os mesmos campos, a mesma base testa várias suspeitas sem nova coleta.
- **Só eventos verificados** numa fonte lida. Os candidatos ainda não verificados ficam numa lista separada, no fim.
- **Campo que depende de documento não lido** fica marcado "a preencher", nunca preenchido por dedução.
- **Cada base termina com "Fontes e consultas":** URL, data, o que foi consultado e os limites.

## 5. Dados e reprodução

- `dados/brutos/` guarda o que veio da fonte, sem edição. Arquivos grandes podem ficar comprimidos (`.gz`).
- Toda tabela de `dados/processados/` sai de um script em `scripts/`. Em 2 nov. 2026, `scripts/senado_analise.py` reproduziu exatamente os CSVs e a Tabela 2 da Base 3.
- Registre a data da coleta. Rodar a coleta de novo muda os números; se isso acontecer, anote a nova data e o que mudou.

## 6. Medidas da Base 3 (saliência dos ministros)

- **Texto analisado:** resumo e indexação redigidos pela equipe do Senado, não o discurso integral. Os textos foram postos em minúsculas e sem acento.
- **Correção de tamanho.** O tamanho médio de resumo e indexação quase dobrou no período, de 53 para 98 palavras. Por isso a medida principal é **ocorrências por 10 mil palavras**, e não a porcentagem de discursos. Sem essa correção, o STF pareceria "mais citado" só porque os resumos cresceram.
- **Ministros por nome.** Entram os nomes sem ambiguidade. Mendonça, Zanin e Dino ficam de fora, porque antes da posse seus nomes aparecem em outros cargos. As contagens são piso: variantes como "Gilmar Ferreira Mendes" não entram.
- **Impeachment, versão estrita.** Conta o discurso quando "impeachment" ou "crime de responsabilidade" aparece no mesmo trecho que o STF ou um ministro. Numa amostra de 12 discursos, cerca de 3 em 4 tratavam de fato do tema.
- **Petições.** Sigla PET no serviço de pesquisa de matérias do Senado. Os totais de 2023 a 2025 foram conferidos no serviço substituto, com os mesmos números.

## 7. Hábitos contra o viés

Registrados na autocrítica de 2 nov. 2026:

1. **Previsões antes dos dados** (`docs/previsoes.md`).
2. **Ler os melhores críticos e os melhores defensores.** Do STF, por exemplo, ler os juristas que questionam os inquéritos abertos pelo próprio tribunal, não os panfletários. Se você não consegue escrever o argumento do outro lado de modo que ele assinaria embaixo, ainda não o entendeu.
3. **Lista de abandono.** Para cada ideia de estimação, o resultado que faria desistir dela (`docs/tese-e-hipoteses.md`, seção 9).
4. **Explicação simples primeiro.** Quando surgir uma explicação mais simples, não releia a hipótese para caber nela. Escreva o que precisaria ser verdade para a hipótese ainda valer e vá checar só isso.
5. **Teste do espelho.** O mecanismo explica os usos de todos os lados, ou de nenhum.
6. **Taxa de base.** Antes de dizer que um caso é singular, compare-o com o conjunto. Em 2025, os EUA impuseram tarifas a quase todo mundo; o singular no caso brasileiro é o motivo político declarado, não a tarifa.
7. **Podar.** Cada hipótese, suspeita, autor ou base precisa mudar alguma previsão; o que não muda vira fundo ou sai.

## 8. Limites gerais conhecidos

- **Um codificador só.** Falta um segundo codificador numa amostra e um livro de códigos.
- **Lado brasileiro mais fraco.** As decisões do STF ainda são citadas por imprensa, não lidas no original.
- **Corroboração.** Vários eventos da linha do tempo têm uma fonte só.
- **Literatura.** A lacuna afirmada na justificativa vem do que foi lido, não de busca sistemática em bases acadêmicas.
- **Caso em movimento.** A data de corte ainda não foi definida.
