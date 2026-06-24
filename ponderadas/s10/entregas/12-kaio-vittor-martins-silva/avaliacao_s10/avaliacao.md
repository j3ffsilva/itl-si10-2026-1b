# Avaliação - Kaio Vittor Martins Silva

Estudante: Kaio Vittor Martins Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

Entregou as quatro partes e executou o bônus. Na Parte 1, descartou o scroll com argumento comportamental ("engajamento menor, chance de converter cai") que não usa nenhum número do notebook para distinguir o scroll do tempo de clique, cuja correlação é menor (r = −0,229 vs. r = +0,485). Essa escolha elevou o MAE de 0,276 para 0,348, diferença que o próprio estudante calculou e reportou. As Partes 3 e 4 citam os índices do modelo com as variáveis escolhidas. A Parte 4 declara que correlação não é causalidade e aponta limitações de sazonalidade e linearidade. O bônus reporta P10 = 5,407%, P90 = 6,292% e interpreta o risco de caudas extremas. A nota fica em 7,5 porque a justificativa da Parte 1 não ancora a escolha nos dados disponíveis.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter com `trendline="ols"` gerado. Scatter matrix adicional. Correlações citadas corretamente (r = −0,643, r = +0,485, r = −0,229). Escolhe `taxa_abandono_carrinho_pct` e `tempo_primeiro_clique_s`, descartando o scroll com argumento comportamental ("usuário rola sem comprar") que contradiz a força da correlação observada (+0,485 vs −0,229) sem evidência numérica adicional.

### Parte 2: Modelo

MAE (0,348) e RMSE (0,452) citados com definições corretas de MAE e RMSE. Contextualiza erro relativo (5,93% da média). Compara com o modelo de 3 variáveis: MAE ≈ 26% maior pela exclusão do scroll. evidência de que a escolha custou qualidade ao modelo, reconhecida pelo próprio estudante.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e tempo). Tabela gerada com índices: abandono −0,511, tempo −0,105. Cita valores e calcula que abandono tem impacto ≈ 4,9× maior que tempo. Tabela e gráfico de barras adicionais. Interpretação correta dentro das variáveis escolhidas.

### Parte 4: Decisão

Recomenda priorizar redução do abandono, cita índice −0,489 (nota: usa o índice do modelo de 3 variáveis mencionado no contexto da atividade, mas seu próprio modelo produziu −0,511. inconsistência menor). Propõe ações concretas (alertas de carrinho, checkout simplificado, barra de progresso). Reconhece explicitamente que "correlação não é causalidade". Limitações: variáveis externas não mapeadas, instabilidade do modelo com sazonalidade, saturação da relação linear. Específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado (modelo com duas variáveis). Estatísticas corretas (média 5,859%, std 0,342, P10 = 5,407%, P90 = 6,292%, amplitude = 0,885 p.p.). Interpreta risco: mesmo no pior decil a conversão fica bem acima do mínimo histórico. Menciona risco de variáveis saírem totalmente do padrão histórico. Interpretação adequada.

## Confiança

Confiança geral: Alta
Observação: a inconsistência no índice de sensibilidade citado na Parte 4 (−0,489 vs −0,511 do próprio modelo) é menor e provavelmente reflexo de ter lido o número do enunciado do problema.
