# Dados

`brutos/` guarda o que veio da fonte, sem edição. `processados/` guarda o que os scripts calculam. Para refazer as tabelas processadas, rode da raiz: `python3 scripts/senado_analise.py`.

## brutos/senado/ (coleta de 2 nov. 2026, `scripts/senado_coleta.py`)

| Arquivo | Conteúdo |
|---|---|
| `pets.json` | 245 petições (sigla PET), 2015–2026. Campos: `Codigo`, `DescricaoIdentificacao`, `Ano`, `Ementa`, `Autor`, `Data`. |
| `proc2023.json`, `proc2024.json`, `proc2025.json` | As mesmas petições no serviço substituto (`/processo`), usadas para conferir os totais. |
| `speeches.json.gz` | 38.461 discursos em plenário, mar. 2017 a out. 2026, comprimidos com gzip. Campos: `id`, `data`, `resumo`, `index` (indexação), `orador`, `partido`. |

## brutos/lda/ (`scripts/lda_coleta.py`)

| Arquivo | Conteúdo |
|---|---|
| `lda_brazil.json` | Relatórios de lobby de 2024–2026 cujo campo de questões específicas cita "Brazil": registrante, cliente, período, valores, URL do documento e trechos. |
| `lda_clients.json` | Trechos sobre censura, Seção 301, Brasil ou DSA nos relatórios de 2025 de X Corp, Rumble, Trump Media, CCIA, NetChoice, Meta e Google. O filtro por nome traz falsos positivos (por exemplo, "Metal" casa com "META"), que foram ignorados. |

## brutos/congresso-eua/

`hr1071_sum.xml` e `hr1071_status.xml`: resumo do CRS e tramitação do H.R. 1071 (*No Censors on our Shores Act*), objeto de lobby do Rumble.

## processados/

| Arquivo | Colunas | Observação |
|---|---|---|
| `senado_peticoes_contra_ministros_STF.csv` | ano, identificacao, data, ministros, ementa | 205 petições contra ministros do STF. |
| `speeches_by_year.csv` | ano, discursos, pct_stf, pct_ministro, contagens por ministro, n_stf, n_ministro | Porcentagem de **discursos** que citam. Os nomes com * são ambíguos antes da posse. |
| `senado_discursos_mensal.csv` | mes, discursos, palavras_resumo_indexacao, discursos_com_STF, discursos_com_ministro_nominal, discursos_com_Moraes | Base da Tabela 3 da Base 3. As palavras permitem normalizar. |
| `senado_mencoes_por_10mil_palavras_anual.csv` | ano, palavras, menções por 10 mil palavras (STF, ministros, Moraes) | Tabela 2 da Base 3: **ocorrências** por 10 mil palavras, a medida principal. |
| `senado_discursos_impeachment_ministros_mensal.csv` | mes, discursos que associam impeachment a ministros ou ao STF | Versão estrita; cerca de 3 em 4 acertos numa amostra de 12. |

Os limites das medidas estão em `docs/metodo.md`, seção 6.
