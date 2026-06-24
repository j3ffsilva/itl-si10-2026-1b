# Avaliação - Cibele Figueredo Leal

Estudante: Cibele Figueredo Leal

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Fez as quatro partes. O modelo usa 3 features com MAE 0,276 e RMSE 0,344; adicionou R² = 0,714 e tabela de coeficientes na Parte 2. A Parte 3 gera a tabela com índices -0,489 e +0,258 e identifica a variável de maior impacto absoluto por código. O bônus executa 1.000 simulações, calcula P5 = 5,221% e P95 = 6,539%, P(conversão > 5%) = 99%, betas padronizados para as 3 variáveis e waterfall chart de receita mensal com premissas explícitas. Três lacunas impedem nota maior: a Parte 1 justifica a escolha de variáveis sem citar os valores -0,643 e +0,485 no texto; a célula de resposta textual da Parte 3 está vazia, com o raciocínio apenas no código; o bônus não gera distribuição do cenário de melhoria nem calcula o ganho médio simulado em p.p.
## Evidência

### Parte 1: Exploração

Matriz de correlação exibida com valores, dois scatter plots (abandono e scroll vs. conversão) com trendline OLS. Justificativa qualitativa: "taxa de abandono chamou atenção por causar o maior impacto", "scroll mostrou que usuários que engajam mais convertem com mais frequência". raciocínio correto mas sem citar os números −0,643 e +0,485 no texto da resposta.

### Parte 2: Modelo

3 features (`features = [abandono, scroll, tempo]`). MAE = 0,276 e RMSE = 0,344 (valores de referência). Calcula R² = 0,7144 (iniciativa além do pedido) e exibe tabela de coeficientes brutos. Interpretação menciona que o erro é baixo "quando comparado com a escala da taxa de conversão" e que RMSE próximo ao MAE indica ausência de erros extremos.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela com índices −0,489 e +0,258. Gráfico de barras dos índices gerado. Célula extra identifica automaticamente a variável de maior impacto absoluto com print formatado. A resposta textual está em branco (célula markdown "Resposta:" vazia); o raciocínio está no código/print.

### Parte 4: Decisão

Recomendação prioriza redução do abandono, cita índice −0,489 e propõe ações (simplificar checkout, reduzir etapas, mostrar frete mais cedo, melhorar desempenho da página). Limitação aponta linearidade do modelo, natureza simulada dos dados e propõe interpretação como "apoio direcional". Não menciona A/B test ou experimento controlado como validação da causalidade assumida.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1.000 amostras, histograma gerado. P5 = 5,221% e P95 = 6,539% calculados no código. Probabilidade P(conversão > 5%) = 99%. Betas padronizados calculados para as 3 variáveis (abandono −0,650, scroll +0,457, tempo −0,328). Simulação financeira adicional (Bônus Executivo): waterfall chart estimando o uplift em receita mensal ao reduzir abandono em 10%, com premissas explícitas (10.000 usuários/dia, ticket R$ 150). Não implementa Monte Carlo comparativo (distribuição do cenário de melhoria vs. baseline) nem calcula ganho médio simulado em p.p.

## Confiança

Confiança geral: Alta
Observação: a avaliação anterior atribuía ao notebook elementos que não estão presentes: cenário Monte Carlo comparativo com "ganho médio de 0,288 p.p.", "P10 sobe de 5,34% para 5,67%", "boxplot comparando cenários" e menção a A/B test na Parte 4. O notebook real tem simulação financeira (waterfall em R$) como extensão do bônus, mas não esses elementos específicos. A nota 9,0 se mantém pelos elementos reais que justificam 4 partes sólidas + bônus com extensão de valor, sem atingir o patamar de 10,0 por ausência do cenário comparativo probabilístico.
