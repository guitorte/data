# Roadmap

A pesquisa anda em fases. A fase atual é a das expedições: cada uma traz dados que ajudam a escolher entre três perguntas possíveis. O manuscrito só volta a andar depois do primeiro ponto de controle.

Legenda: `[x]` feito · `[ ]` a fazer · `[~]` em andamento ou parcial.

## Fase 0 · Fundação (29 out. a 1º nov. 2026) — concluída

- [x] Pergunta, tese e hipóteses iniciais (H1 a H4, mais a hipótese rival)
- [x] Referencial teórico com os livros lidos na íntegra ou em parte (lista em `fontes/livros.md`)
- [x] Linha do tempo Brasil–EUA, 2024 a 2026, com 47 eventos (`dossies/linha-do-tempo-brasil-eua.md`)
- [x] Rascunho do artigo, seções 1 a 10, com notas numeradas e referências em ABNT (`manuscrito/rascunho-artigo.md`)
- [x] Perguntas para o NotebookLM (`notebooklm/perguntas.md`)

## Fase 1 · Expedições (desde 2 nov. 2026) — em andamento

O documento deixou de ser o produto e virou acampamento-base. Cada expedição volta com dados e os guarda numa base ou dossiê.

### Feitas

- [x] **Dossiê da Seção 301.** O processo comercial americano lido no original: avisos, audiências, relatórios anuais e registros de lobby. Derrubou a H3b. (`dossies/secao-301.md`)
- [x] **Balanço dos achados,** com grau de certeza (`docs/achados.md`)
- [~] **Base 1 · Aplicação no Brasil.** Esqueleto com os casos verificados; vários campos "a preencher". (`bases/base1-aplicacao-no-brasil.md`)
- [x] **Base 2 · Instrumentos do país-sede,** de 2019 a 2026 (`bases/base2-instrumentos-pais-sede.md`)
- [x] **Base 3 · Saliência dos ministros,** com dados do Senado (`bases/base3-saliencia-ministros.md`)
- [x] **Migração para o GitHub** (este repositório)

### Próximas, em ordem sugerida

1. [~] **Pôr o repositório de pé.** Repositório `guitorte/data` criado e arquivos enviados em 2 nov. 2026. Falta uma primeira sessão no Claude Code que leia o `CLAUDE.md` e o `estado-atual.md`.
2. [~] **Tramitação dos projetos sobre plataformas.** A pergunta é se a lei vira prazo (suspeita 9). Previsão P2 registrada em 2 nov. 2026. Etapas, com o esforço recomendado entre parênteses:
   - [~] 2.1 Protocolo, antes de abrir os dados: definições, regra de seleção, grupo de controle, janela eleitoral (alto). Versão 1 escrita em `docs/protocolos/tramitacao.md`, aguardando aprovação.
   - [ ] 2.2 Coleta da tramitação do PL 2630 no Senado e na Câmara, por script (baixo)
   - [ ] 2.3 Linha do tempo do PL 2630: intervalos parados, pautas, urgências (médio)
   - [ ] 2.4 O que veio antes de cada adiamento relevante: campanhas, eleições, crises, com fontes datadas (alto)
   - [ ] **Pausa:** um caso só não testa a P2; decidir se vale montar o universo de projetos
   - [ ] 2.5 Universo de projetos sobre plataformas e grupo de controle: seleção e coleta (médio)
   - [ ] 2.6 Comparação e teste da P2, com grau de certeza (alto)
   - [ ] 2.7 Registro: base, fontes, achados, estado atual, commit (baixo)
3. [ ] **Base 3 ampliada.**
   - Discursos da Câmara, que têm texto integral.
   - Quem fala dos ministros, e por qual partido.
   - Explicar os picos sem causa identificada: abr. 2022, set. 2025 e set. 2026.
   - Conferir em fonte própria a decisão de Gilmar Mendes de dez. 2025 sobre quem pode pedir impeachment.
4. [ ] **Canadá × Brasil.** O Canadá revogou o imposto digital dois dias depois de Trump cortar as negociações; o Brasil pagou a tarifa e não recuou. Por que um Estado cede e outro não?
5. [ ] **Lacunas da Base 1.**
   - Decisões originais do STF sobre o X e o Rumble.
   - O episódio do Telegram em 2023.
   - As ordens do TSE e as da Anatel.
6. [ ] **Comentários escritos da Seção 301** do X, do Rumble e do CCB-USA. O portal bloqueia leitura automatizada, então o download é manual (usuário).

### Em espera (só se o ponto de controle pedir)

- [ ] **Corpus datado de linguagem.** Onde nascem e como se espalham "ordens secretas", "censura", "caça às bruxas", "fraude" (H4 e suspeitas 1, 4 e 8).
- [ ] **Dependência de mercado.** Usuários e receita por país e plataforma (H1 e suspeita 11).
- [ ] **Estudo de evento das conexões políticas no 26 out. 2026.** As empresas ligadas à campanha derrotada caíram mais que as comparáveis?
- [ ] **Revisão sistemática de literatura,** começando pelos nomes citados de memória e ainda não conferidos: Culpepper e Thelen; Vilhena Vieira ("Supremocracia"); Arguelhes e Ribeiro ("Ministrocracia").
- [ ] **Aliado vencedor × aliado derrotado:** Argentina, 2025 (de memória, conferir).

## Ponto de controle 1 — depois dos itens 2 e 3

Parar, olhar o conjunto e decidir:

- [ ] Atualizar `docs/achados.md`.
- [ ] **Escolher a pergunta do trabalho:**
  - soberania: como um Estado sustenta a aplicação da lei sob pressão externa;
  - adoção pelo país-sede: quando e por que um governo compra a briga de suas plataformas;
  - obediência: quando as plataformas cumprem.
- [ ] Registrar com data a previsão do aliado derrotado: a derrota rende (suspeita 7) ou o contrato acaba (suspeita 16). Ver `docs/previsoes.md`.
- [ ] **Podar.** Para cada hipótese, suspeita, autor e base, perguntar: muda alguma previsão? O que não muda vira fundo ou sai.
- [ ] Escrever a **lista de abandono:** para cada ideia de estimação (por exemplo, "ideologia de aluguel"), o resultado que faria desistir dela.

## Fase 2 · Manuscrito

- [ ] Reescrever a seção 2 com a pergunta e a tese escolhidas; ajustar introdução e título.
- [ ] Cortar para um argumento só. O texto atual tenta ser três artigos (multa × exclusão; escalada; enquadramento narrativo).
- [ ] Trocar "Resultados esperados" por resultados.
- [ ] Material de replicação: bases publicadas, livro de códigos e segundo codificador numa amostra.
- [ ] Conferir as páginas dos e-books sem paginação numa edição impressa.
- [ ] Definir data de corte, revista-alvo e idioma (inglês, se o alvo for internacional).

## Fase 3 · Programa de pesquisa

A narrativa inteira é um programa, não um artigo. Os trechos possíveis, do mais pronto ao mais especulativo:

1. **O cruzamento:** Brasil, do X em 2024 à Seção 301 em 2026. O país-sede adota a queixa, e o aliado é descartável.
2. **Ideologia de aluguel:** os momentos em que interesse e ideologia se separam.
3. **Desorientação como recurso:** a H4, com análise de conteúdo.
4. **Mercados e eleições:** o estudo de evento, como aposta especulativa.
5. **O ensaio ou livro,** escrito depois que dois ou três trechos estiverem pavimentados.
