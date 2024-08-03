## 2. Testes de Hipóteses em Python

Vamos explorar os testes de hipóteses, uma ferramenta poderosa para analisar dados e tirar conclusões significativas.

### 2.1 Definição de Hipóteses Nulas e Alternativas

Em testes de hipóteses, queremos verificar se há evidências suficientes para rejeitar uma declaração inicial sobre uma população. Essa declaração inicial é chamada de ****hipótese nula (H0)****, que geralmente assume que não há efeito ou diferença significativa.

Por outro lado, a ****hipótese alternativa (H1)**** é a declaração que estamos tentando provar. Ela representa o oposto da hipótese nula, assumindo que há um efeito ou diferença significativa.

- **Exemplo:**
    - **H0:** A média de altura dos alunos de uma escola é 1,70m.
    - **H1:** A média de altura dos alunos de uma escola é diferente de 1,70m.

### 2.2 Tipos de Testes de Hipóteses

Existem vários tipos de testes de hipóteses, cada um adequado para diferentes tipos de dados e cenários:

#### 2.2.1. Teste t de Student

- **Objetivo:** O processo envolve comparar a média de uma amostra específica com um valor de referência, que é geralmente retirado de uma população maior. Isso permite uma melhor compreensão do posicionamento da amostra em relação à população como um todo. Além disso, é possível comparar as médias de duas amostras independentes. Este método de comparação é útil para determinar se há diferenças significativas entre as duas amostras, o que pode ser crucial para a análise de dados.
- **Requisitos:** É essencial que os dados apresentem uma distribuição normal ou, alternativamente, que o tamanho da amostra seja suficientemente grande para permitir a aplicação do Teorema do Limite Central. Este teorema é uma ferramenta estatística fundamental que permite fazer inferências sobre a população a partir de amostras. Portanto, é crucial garantir que essas condições sejam atendidas antes de prosseguir com a análise.

    - **Exemplo:** Comparar a média de altura de uma turma com a média nacional.

- **Código:**

```python
from scipy.stats import ttest_1samp

# Dados da amostra
data = [22, 21, 24, 25, 20, 23, 19, 20, 21, 23]

# Teste de hipóteses
# * H0: A média é igual a 20
# * H1: A média é diferente de 20

t_statistic, p_value = ttest_1samp(data, 20) # Realiza o teste t de uma amostra, comparando os dados da amostra com a média populacional (20)

print("Estatística t:", t_statistic) #Estatística t: 2.9459415181858977
print("Valor p:", p_value) #Valor p: 0.01632827323949718
```

-   Interpretação:

O valor p (0.0163) é menor que o nível de significância usual de 0.05. Isso significa que existe evidência suficiente para rejeitar a hipótese nula e concluir que a média da população é diferente de 20. A estatística t (2.9459) indica que a média da amostra é significativamente diferente da média populacional hipotética.

#### 2.2.2. Teste Z

- **Objetivo:** Este teste é utilizado quando o objetivo é comparar uma proporção de uma amostra com um valor de referência que é conhecido da população. Também pode ser usado para comparar as proporções de duas amostras independentes.

- **Requisitos:** O Teste Z tem alguns requisitos importantes. Primeiramente, a distribuição da proporção populacional deve ser normal ou, alternativamente, o tamanho da amostra deve ser grande o suficiente para que possamos aplicar o Teorema do Limite Central.

    - **Exemplo:** Comparar a proporção de clientes satisfeitos com um novo produto com a proporção de clientes satisfeitos com o produto antigo.

- **Código:**

```python
from statsmodels.stats.proportion import proportions_ztest

# Dados
n = 100  # Tamanho da amostra
x = 85   # Número de sucessos (clientes satisfeitos)
p0 = 0.75  # Proporção a ser testada

# Teste de hipóteses
# * H0: A proporção é igual a p0
# * H1: A proporção é maior que p0

stat, p_value = proportions_ztest(count=x, nobs=n, value=p0, alternative='larger') #Realiza o teste z de proporções usando a função proportions_ztest. A função recebe como argumentos o número de sucessos (count), o tamanho da amostra (nobs), a proporção hipotética (value) e a hipótese alternativa (alternative). Retorna a estatística z e o valor p.

print("Estatística Z:", stat) #Estatística Z: 2.800560168056019
print("Valor p:", p_value) #Valor p: 0.002550699823002496
```

-   Interpretação:

O valor p (0.0025) é menor que o nível de significância usual de 0.05. Isso significa que existe evidência suficiente para rejeitar a hipótese nula e concluir que a proporção de clientes satisfeitos é maior que 0.75. A estatística z (2.8005) indica que a proporção da amostra é significativamente maior que a proporção populacional hipotética.

#### 2.2.3. Teste Qui-Quadrado

- **Objetivo:** Esta análise serve para ver se duas variáveis categóricas são independentes. Queremos saber se quando algo acontece em uma variável, isso afeta o que acontece na outra. Para isso, faremos testes estatísticos. Esses testes vão mostrar se as variáveis estão relacionadas por acaso ou se existe uma relação real.

- **Requisitos:** É necessário que os dados de frequência estejam organizados de maneira clara e compreensível em uma tabela de contingência. Esta tabela deve apresentar todas as variáveis relevantes e suas respectivas contagens de frequência, permitindo assim uma análise estatística precisa e eficaz.

    - **Exemplo:** Verificar se há associação entre gênero e preferência por um determinado tipo de filme.

- **Código:**

```python
import numpy as np
from scipy.stats import chi2_contingency

# Dados (tabela de contingência)
observed = np.array([[50, 30, 20], [40, 35, 25]])  # Frequência observada

# Teste de hipóteses
chi2_stat, p_value, dof, expected = chi2_contingency(observed) #Realiza o teste qui-quadrado de independência usando a função chi2_contingency. A função recebe a tabela de contingência (observed) como argumento e retorna a estatística qui-quadrado, o valor p, os graus de liberdade e a tabela de frequências esperadas.

print("Estatística Qui-Quadrado:", chi2_stat) #Estatística Qui-Quadrado: 2.051282051282051
print("Valor p:", p_value) #Valor p: 0.3585665413731905
```
-   Interpretação:

O valor p (0.3586) é maior que o nível de significância usual de 0.05. Isso significa que não existe evidência suficiente para rejeitar a hipótese nula de independência entre as variáveis. Ou seja, não há evidência significativa para afirmar que as variáveis ​​estão relacionadas. A estatística qui-quadrado (2.0513) indica que a diferença entre as frequências observadas e as frequências esperadas é relativamente pequena.

- Observação: A função chi2_contingency também retorna os graus de liberdade (dof) e a tabela de frequências esperadas (expected). Os graus de liberdade são calculados como (número de linhas - 1) * (número de colunas - 1). As frequências esperadas são calculadas assumindo independência entre as variáveis.

#### 2.2.4. Teste ANOVA

- **Objetivo:** O objetivo principal do nosso estudo é realizar uma comparação detalhada das médias de três ou mais grupos que são independentes entre si. Isso envolve uma análise cuidadosa para entender as diferenças e semelhanças entre esses grupos, considerando a variabilidade dentro de cada um deles.

- **Requisitos:** Os dados devem ser normalmente distribuídos, ou seja, os dados de cada grupo devem ser igualmente distribuídos em torno da média. Também, as diferenças entre os grupos devem ser iguais, o que garante que os dados são consistentes. Por fim, as amostras devem ser independentes, o que significa que um evento não influencia outro.

    - **Exemplo:** Comparar a média de altura de estudantes em três diferentes escolas.

- **Código:**

```python
from scipy.stats import f_oneway

# Dados
group1 = [170, 172, 168, 171, 175]  # Alturas do grupo 1
group2 = [165, 168, 170, 166, 169]  # Alturas do grupo 2
group3 = [172, 175, 178, 176, 174]  # Alturas do grupo 3

# Teste de hipóteses
f_stat, p_value = f_oneway(group1, group2, group3) # Realiza o teste F de uma via usando a função f_oneway. A função recebe as listas de dados como argumentos e retorna a estatística F e o valor p.

print("Estatística F:", f_stat) #Estatística F: 12.8375
print("Valor p:", p_value) #Valor p: 0.001044162063483525
```

-   Interpretação:

O valor p (0.0010) é menor que o nível de significância usual de 0.05. Isso significa que existe evidência suficiente para rejeitar a hipótese nula de que as médias dos grupos são iguais. Ou seja, há evidência significativa para afirmar que existe diferença entre as médias dos grupos. A estatística F (12.8375) indica que a variância entre os grupos é relativamente alta em comparação com a variância dentro dos grupos.

### 2.3. Erros Tipo I e Tipo II

Quando nos propomos a realizar testes de hipóteses, é importante estar ciente de que existe o risco inevitável de tomarmos decisões erradas. Esse risco é representado por dois tipos principais de erros.

- **Erro Tipo I (Falso Positivo):** Este ocorre quando rejeitamos a hipótese nula, mesmo quando ela é verdadeira. Em outras palavras, estamos acreditando que há um efeito ou diferença quando, na realidade, não existe.

- **Erro Tipo II (Falso Negativo):** Isto é, não rejeitamos a hipótese nula quando ela é, de fato, falsa. Nesse caso, estamos ignorando um efeito ou diferença que realmente existe.

### 2.4.Níveis de Significância

O nível de significância, também conhecido como alfa (α), é um conceito fundamental na estatística que se refere à probabilidade de cometer um erro tipo I, ou seja, a probabilidade de rejeitar erroneamente a hipótese nula quando ela é verdadeira. Este erro ocorre quando concluímos que existe uma relação significativa entre duas variáveis, quando na realidade, essa relação não existe. O nível de significância é uma medida de tolerância ao risco e é geralmente definido em 0.05 ou 0.01, dependendo do grau de certeza que queremos ter em nossas conclusões. Se definido em 0.05, estamos dispostos a aceitar um risco de 5% de rejeitar a hipótese nula quando ela é verdadeira. Se for definido em 0.01, o risco desce para 1%.

### 2.5. Interpretação dos Resultados

- **Valor p:** Este é um conceito muito importante na estatística. O valor p é a probabilidade de se obter um resultado tão extremo quanto o observado, se a hipótese nula for verdadeira. Em outras palavras, é uma medida de evidência contra a hipótese nula. Quanto menor o valor p, mais forte é a evidência de que devemos rejeitar a hipótese nula.

- **Rejeição da hipótese nula:** No contexto da análise estatística, se observarmos que o valor p é menor que o nível de significância (α), então temos evidência suficiente para rejeitar a hipótese nula. Isso significa que temos razões fortes para acreditar que a hipótese nula, que é a nossa suposição inicial, pode não ser verdadeira. No entanto, é importante notar que rejeitar a hipótese nula não necessariamente prova que a alternativa é verdadeira. Simplesmente indica que, dados os dados disponíveis e o nível de significância escolhido, a hipótese nula não é a explicação mais provável.

- **Não rejeição da hipótese nula:** Quando realizamos um teste de hipóteses, estamos essencialmente tentando tomar uma decisão sobre uma afirmação específica. O valor P desempenha um papel crucial nesse processo. Se o valor P obtido através do nosso teste estatístico for maior que o nível de significância pré-definido (α), então a decisão que tomamos é de não rejeitar a hipótese nula. Em outras palavras, a evidência disponível não é suficientemente forte para nos fazer acreditar que a hipótese nula é falsa.

### Conclusão

Lembrem-se de que a escolha do teste adequado e a interpretação correta dos resultados são essenciais para tirar conclusões significativas a partir dos dados.

- **Lembre-se:**
    - Utilize as bibliotecas Python como Scipy, Statsmodels ou Numpy para realizar os cálculos necessários.
    - Anote as hipóteses nulas e alternativas para cada teste.
    - Escolha o nível de significância apropriado para cada teste.
    - Interprete os resultados dos testes e conclua se há evidências suficientes para rejeitar ou não a hipótese nula.

- **Recursos Adicionais:**
    - [Documentação Scipy](https://docs.scipy.org/doc/scipy/reference/index.html)
    - [Documentação Statsmodels](https://www.statsmodels.org/stable/index.html)
    - [Documentação Numpy](https://numpy.org/doc/stable/)