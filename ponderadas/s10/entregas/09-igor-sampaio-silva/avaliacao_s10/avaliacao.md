# Avaliação - Igor Sampaio Silva

Estudante: Igor Sampaio Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

Entregou as quatro partes e executou o bônus. Na Parte 1, descartou o scroll em favor do tempo de clique com argumento comportamental ("rolar sem comprar") que não está ancorado em nenhum número do notebook e contradiz a correlação observada (r = +0,485 para scroll vs. r = −0,229 para tempo de clique). Essa escolha excluiu a segunda variável mais relevante e elevou o MAE do modelo de 0,276 para 0,348. As Partes 3 e 4 citam índices do próprio modelo e a Parte 4 menciona explicitamente que correlação não é causalidade. A nota fica em 7,5 porque a justificativa da Parte 1 não usa os dados para sustentar a escolha, o que compromete a análise das partes seguintes.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter e scatter matrix gerados. Cita correlações corretamente (r = −0,643, r = +0,485, r = −0,229). Porém escolhe `tempo_primeiro_clique_s` como segunda variável em vez de scroll, justificando com argumento comportamental não sustentado pelos números ("rolar sem comprar"). Justificativa não tem âncora numérica que distinga tempo de clique do scroll.

### Parte 2: Modelo

MAE (0,348) e RMSE (0,452) citados e explicados com definições corretas de MAE e RMSE. Contextualiza o erro em relação à média (5,87%) e menciona que o custo de excluir o scroll foi MAE ≈ 26% maior. Interpretação adequada, mas o modelo é subótimo pela escolha de variáveis.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida com abandono e tempo de clique. Tabela gerada com índices: abandono −0,511 e tempo −0,105. Cita valores da tabela e calcula que o abandono tem impacto ≈ 4,9× maior que o tempo. Interpretação correta dentro das variáveis escolhidas. Índice do abandono ligeiramente diferente dos demais (−0,511 vs −0,489) porque o modelo exclui scroll, redistribuindo os coeficientes.

### Parte 4: Decisão

Recomenda priorizar redução do abandono com índice −0,489 citado (nota: no corpo da resposta usa o índice do modelo completo do contexto, não o −0,511 do seu próprio modelo. inconsistência menor). Propõe ações concretas (alertas de carrinho, checkout simplificado, barra de progresso). Limitações: correlação não é causalidade (explicitamente mencionada), instabilidade do modelo com sazonalidade, e ponto de saturação da relação linear. As três limitações são específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado (modelo com duas variáveis). Estatísticas corretas para o modelo escolhido (média 5,859%, P10 = 5,407%, P90 = 6,292%). Cita amplitude P10–P90 = 0,885 p.p. e interpreta risco de caudas extremas quando variáveis saem do padrão histórico. Interpretação adequada.

## Confiança

Confiança geral: Alta
Observação: a inconsistência do índice citado na Parte 4 (−0,489 em vez de −0,511) é menor e pode ser interpretada como referência ao valor da exploração pré-escolha de variáveis.
