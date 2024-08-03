# 1.1 Teste t para Comparar Médias de Dois Grupos

O teste t para amostras independentes é uma ferramenta estatística fundamental para comparar as médias de dois grupos distintos quando você deseja determinar se há uma diferença significativa entre elas. Ele é amplamente utilizado em pesquisas de mercado, estudos científicos e análise de dados em diversas áreas, pois permite avaliar se a diferença observada entre as médias é apenas uma variação aleatória ou se representa uma diferença real entre as populações que as amostras representam.

**Objetivo:** Determinar se há uma diferença significativa na média de duas populações, com base em amostras independentes.

**Cenário Exemplo:** Comparar a altura média de jogadores de basquete de dois times diferentes (Time A e Time B).

**Hipóteses:**

* **H0 (Hipótese Nula):** Não há diferença significativa na altura média dos jogadores dos dois times.
* **H1 (Hipótese Alternativa):** Há uma diferença significativa na altura média dos jogadores dos dois times.

**Dados:** Coleta de dados sobre a altura dos jogadores de cada time, incluindo a média (x̄) e o desvio padrão (s) de cada amostra.

**Teste t para Amostras Independentes:**

* **Fórmula:**

   ```
   t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
   ```

   Onde:
    * x̄₁ e x̄₂ são as médias das amostras dos dois grupos
    * s₁² e s₂² são as variâncias das amostras dos dois grupos
    * n₁ e n₂ são os tamanhos das amostras dos dois grupos

* **Lógica:** A fórmula calcula uma estatística t, que representa a diferença entre as médias dos grupos, ajustada pela variabilidade dentro de cada grupo. Quanto maior a diferença entre as médias e menor a variabilidade, maior a estatística t e mais forte a evidência contra a hipótese nula.

* **Interpretação:**

    * **Valor-p:**  É a probabilidade de obter uma diferença entre as médias tão grande quanto a observada, assumindo que a hipótese nula é verdadeira.
    * **Rejeição da Hipótese Nula:** Se o valor-p for menor que o nível de significância α (geralmente 0.05), rejeitamos H0 e concluímos que há uma diferença significativa entre as médias.
    * **Falha na Rejeição da Hipótese Nula:** Se o valor-p for maior que α, não rejeitamos H0. Não há evidências suficientes para concluir que existe uma diferença significativa entre as médias.

**Exemplo:**

* Comparar a altura média de homens e mulheres.
* **Dados:**
    * x̄₁ (Homens) = 1,75 m
    * x̄₂ (Mulheres) = 1,65 m
    * s₁² (Homens) = 0,05 m²
    * s₂² (Mulheres) = 0,04 m²
    * n₁ (Homens) = 100
    * n₂ (Mulheres) = 100

* **Cálculo da Estatística t:**

    ```
    t = (1,75 - 1,65) / √(0,05²/100 + 0,04²/100) 
    t = 0,1 / √(0,000025 + 0,000016)
    t = 0,1 / √0,000041
    t ≈ 1,55
    ```

* **Determinando o Valor-p:**

    * Consulta a uma tabela t ou software estatístico com graus de liberdade (df) = n₁ + n₂ - 2 = 198.
    * O valor-p para t ≈ 1,55 é aproximadamente 0,12.

* **Interpretação:**

    * O valor-p (0,12) é maior que α (0,05). 
    * Portanto, não rejeitamos a hipótese nula. 
    * Não há evidências suficientes para concluir que a altura média dos homens é diferente da altura média das mulheres.

**Observação:** A escolha do nível de significância α (geralmente 0.05) depende do contexto da pesquisa e do nível de risco que o pesquisador está disposto a assumir.

**Conclusão:** O teste t para amostras independentes é uma ferramenta poderosa para comparar médias de duas populações, permitindo que os pesquisadores determinem se há uma diferença significativa entre elas.  