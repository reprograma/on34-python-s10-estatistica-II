<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Estatística com python - testes de hipóteses

Turma Online On34 | Python | Semana 10 | 2024 | <a href="https://www.linkedin.com/in/stefanygbsilva/" target="_blank" rel="noopener noreferrer">Professora Stefany Gracy</a>

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]


## Índice

- **1. Testes de Hipóteses**
    - [**1.1 Definição de Hipóteses Nulas e Alternativas**](capitulos/testes_hipoteses.md#11-definicao-de-hipoteses-nulas-e-alternativas)
    - [**1.2 Tipos de Testes de Hipóteses**](capitulos/testes_hipoteses.md#12-tipos-de-testes-de-hipoteses)
        - [**1.2.1 Teste t de Student**](capitulos/testes_hipoteses.md#121-teste-t-de-student)
            - [**1.2.1.1 Teste t de uma amostra**](capitulos/testes_hipoteses.md#1211-teste-t-de-uma-amostra)
            - [**1.2.1.2 Teste t de duas amostras**](capitulos/testes_hipoteses.md#1212-teste-t-de-duas-amostras)
        - [**1.2.2 Teste Z**](capitulos/testes_hipoteses.md#122-teste-z)
            - [**1.2.2.1 Teste Z de uma proporção**](capitulos/testes_hipoteses.md#1221-teste-z-de-uma-proporcao)
            - [**1.2.2.2 Teste Z de duas proporções**](capitulos/testes_hipoteses.md#1222-teste-z-de-duas-proporcoes)
        - [**1.2.3 Teste Qui-Quadrado**](capitulos/testes_hipoteses.md#123-teste-qui-quadrado)
        - [**1.2.4 Teste ANOVA**](capitulos/testes_hipoteses.md#124-teste-anova)
    - [**1.3 Erros Tipo I e Tipo II**](capitulos/testes_hipoteses.md#13-erros-tipo-i-e-tipo-ii)
    - [**1.4 Níveis de Significância**](capitulos/testes_hipoteses.md#14-niveis-de-significancia)
    - [**1.5 Interpretação dos Resultados**](capitulos/testes_hipoteses.md#15-interpretacao-dos-resultados)
    - [**1.6 Em Resumo**](capitulos/testes_hipoteses.md#16-em-resumo)
- **2. Testes de Hipóteses em Python**
    - [**2.1 Definição de Hipóteses Nulas e Alternativas**](capitulos/testes_pyhton.md#21-definicao-de-hipoteses-nulas-e-alternativas)
    - [**2.2 Tipos de Testes de Hipóteses**](capitulos/testes_pyhton.md#22-tipos-de-testes-de-hipoteses)
        - [**2.2.1 Teste t de Student**](capitulos/testes_pyhton.md#221-teste-t-de-student)
        - [**2.2.2 Teste Z**](capitulos/testes_pyhton.md#222-teste-z)
        - [**2.2.3 Teste Qui-Quadrado**](capitulos/testes_pyhton.md#223-teste-qui-quadrado)
        - [**2.2.4 Teste ANOVA**](capitulos/testes_pyhton.md#224-teste-anova)
    - [**2.3 Erros Tipo I e Tipo II**](capitulos/testes_pyhton.md#23-erros-tipo-i-e-tipo-ii)
    - [**2.4 Níveis de Significância**](capitulos/testes_pyhton.md#24-niveis-de-significancia)
    - [**2.5 Interpretação dos Resultados**](capitulos/testes_pyhton.md#25-interpretacao-dos-resultados)
    - [**2.6 Em Resumo**](capitulos/testes_pyhton.md#26-em-resumo))

- **3. Testes Individuais**
    - **3.1 Teste t** 
        - [**3.1.1 Teste t para Amostras Independentes:**](capitulos/testes/testet.md)
    - **3.2 Teste Z**
        - [**3.2.1 Teste Z para Comparar Proporções:**](capitulos/testes/testez.md)
    - **3.3 Teste Qui-quadrado**
        - [**3.3.1 Teste Qui-quadrado de Independência:**](capitulos/testes/qui.md)
    - **3.4 Teste ANOVA**
        - [**3.4.1 Teste ANOVA:**](capitulos/testes/anova.md)

***
### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)

### Material da aula 

### Links Úteis
**Implementação em Python:**

* **[Documentação Scipy](https://docs.scipy.org/doc/scipy/reference/index.html)**: Documentação completa da biblioteca Scipy, incluindo funções para testes estatísticos.
* **[Documentação Statsmodels](https://www.statsmodels.org/stable/index.html)**: Documentação da biblioteca Statsmodels, com foco em testes estatísticos e modelos estatísticos.
* **[Documentação Numpy](https://numpy.org/doc/stable/)**: Documentação da biblioteca Numpy para manipulação de arrays e matrizes em Python.
* **[Doc Random](https://docs.python.org/pt-br/3/library/random.html)** : Documentação da biblioteca Random para gerar números aleatórios em Python.


<p align="center">
Desenvolvido com :purple_heart:  
</p>

