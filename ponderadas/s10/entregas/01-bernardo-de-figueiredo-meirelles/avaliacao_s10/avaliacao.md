# Avaliação - Bernardo de Figueiredo Meirelles

Estudante: Bernardo de Figueiredo Meirelles

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

Entregou as quatro partes com iniciativas técnicas além do pedido: heatmap de correlação, gráfico de resíduos e Monte Carlo com histograma. A recomendação de produto aponta o abandono do carrinho como alvo. O problema central está na Parte 1: o texto cita correlações de "−0,78" para abandono e "−0,35" para tempo de clique, mas a matriz exibida no próprio notebook mostra −0,643 e −0,229. Os números não existem nos dados. O bônus executa as 1000 simulações e calcula P10 ≈ 5,37% e P90 ≈ 6,38%, mas a interpretação textual não cita esses percentis. A nota 7,5 decorre da âncora numérica incorreta na Parte 1, que é a justificativa da escolha de variáveis.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`; scatter e heatmap de correlação gerados. Escolheu abandono do carrinho e tempo do primeiro clique. A justificativa cita correlações de "−0,78" e "−0,35" que não existem na matriz exibida pelo notebook (valores reais: −0,643 e −0,229). O argumento qualitativo ("usuário com a carteira na mão") é contextual mas não se apoia nos números corretos.

### Parte 2: Modelo

MAE 0,276 e RMSE 0,344 obtidos e exibidos. Gráfico de resíduos adicionado (iniciativa além do pedido). A interpretação é vaga: diz que os erros são "baixos" e que "RMSE não está longe do MAE", mas não compara o MAE com a escala da variável alvo (~5,87%) para quantificar a aceitabilidade.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida com abandono e tempo do primeiro clique. Tabela gerada: índice −0,489 para abandono e −0,112 para tempo. Os índices estão corretos para as variáveis escolhidas. A interpretação cita o coeficiente do modelo (−0,055) em vez dos índices de sensibilidade da tabela, misturando dois conceitos distintos. A conclusão (abandono tem maior impacto) está correta.

### Parte 4: Decisão

Recomendação de simplificar o pagamento e deixar o frete claro é específica e acionável. Aponta limitação de linearidade e possível interação entre variáveis (abandono podendo ser influenciado pelo scroll). Não distingue explicitamente associação de causalidade no texto.

### Ao Além dos Aléns (bônus)

Presente e executado: 1000 simulações, histograma produzido, percentis P10/P90 calculados (5,37% e 6,38%). A interpretação textual, porém, é superficial. menciona "dispersão apertada" sem citar os percentis calculados ou conectá-los ao risco da recomendação. Adicionou também gráfico de Monte Carlo com linhas de percentil e análise de impacto financeiro estimado (iniciativa criativa e relevante para decisão de produto).

## Confiança

Confiança geral: Alta

Observação: as correlações fabricadas na Parte 1 são verificáveis pela matriz exibida no próprio notebook, o que torna o desvio inequívoco.
