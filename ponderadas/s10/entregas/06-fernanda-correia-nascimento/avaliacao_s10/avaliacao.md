# Avaliação - Fernanda Correia Nascimento

Estudante: Fernanda Correia Nascimento

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

Entregou as quatro partes. A Parte 1 é a mais detalhada do lote: scatter painel com três variáveis, boxplots por tercil e perfil top/bottom 10% com tabela (abandono 39,48% vs. 55,34%). A Parte 2 compara MAE com a amplitude da variável alvo ("~7% da amplitude total"). A Parte 4 aponta interação entre variáveis e distingue associação de causalidade. Dois erros factuais penalizam a nota: na Parte 3, o texto cita índices "−0,63" e "+0,40", mas a tabela gerada pelo notebook mostra −0,489 e +0,258, diferença de ~29% e ~55%; no bônus, o texto cita P10 ≈ 3,5%, P50 ≈ 4,3% e P90 ≈ 5,2%, mas a simulação de 10.000 amostras mostra P10 ≈ 5,38%, P50 ≈ 5,87% e P90 ≈ 6,37%. Os três percentis citados não correspondem aos calculados. A nota 8,0 aplica o mesmo critério de Bernardo: números incorretos no texto autoral em partes centrais impedem nota acima desse valor.

## Evidência

### Parte 1: Exploração

Quatro análises exploratórias: scatter painel com três variáveis coloridas por conversão, boxplots por tercil de cada variável, perfil top/bottom 10% com tabela (abandono 39,48% vs. 55,34%). Correlações corretas: −0,643 e +0,485. Exploração mais detalhada do lote.

### Parte 2: Modelo

MAE 0,276, RMSE 0,344. Interpreta MAE como "~7% da amplitude total" (~4 p.p.) e comenta que RMSE pouco acima do MAE é esperado dado o processo gerador linear com ruído gaussiano. Âncora numérica presente e correta.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). Análise adicional com variações de ±10% e ±20%, confirmando linearidade e simetria. O texto autoral, contudo, cita "−0,63" e "+0,40". diferença de ~29% e ~55% em relação aos valores da tabela. Erro factual em parte central da entrega.

### Parte 4: Decisão

Recomendação estruturada com três ações específicas. Limitação mais sofisticada do lote: aponta interação entre variáveis, distinção explícita de associação vs. causalidade, efeitos conjuntos não capturados pelo modelo. A recomendação reitera os índices incorretos (−0,63 e +0,40), propagando o erro da Parte 3.

### Ao Além dos Aléns (bônus)

10.000 simulações com justificativa explícita. Tabela com P10–P90 gerada pelo notebook: P10 ≈ 5,38%, P50 ≈ 5,87%, P90 ≈ 6,37%. O texto, contudo, cita P50 ≈ 4,3%, P10 ≈ 3,5% e P90 ≈ 5,2%. valores incompatíveis com a distribuição gerada (centrada em ~5,87%, não em ~4,3%). Erro factual no bônus: os três percentis citados não correspondem aos calculados.

## Confiança

Confiança geral: Alta

Observação: duas inconsistências verificáveis diretamente no notebook. índices da Parte 3 e percentis do Monte Carlo citados no texto diferem dos valores computados. Aplicado o mesmo critério usado para Bernardo (7,5 por correlações erradas no texto): dois pontos de erro em partes centrais justificam 8,0.
