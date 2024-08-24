from scipy.stats import chi2_contingency

dados = [[30, 40],
         [20, 10]]

r = chi2_contingency(dados)

significancia = 0.05

if r.pvalue < significancia:
    print("Rejeitamos a hipótese nula. Existe uma relação significativa entre a cidade e a preferência pela bebida.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que existe uma relação significativa entre a cidade e a preferência pela bebida.")

print(f"Valor p: {r.pvalue:.5f}")
print(f"Estatística: {r.statistic:.5f}")
print(f"Graus de liberdade:: {r.dof:.5f}")
print("Frequências esperadas:")
for linha in r.expected_freq:
    print(linha)
print(f"Nível de significância: {significancia:.2f}")

# Rejeitamos a hipótese nula. Existe uma relação significativa entre a cidade e a preferência pela bebida.
# Valor p: 0.04953
# Estatística: 3.85714
# Graus de liberdade:: 1.00000
# Frequências esperadas:
# [35. 35.]
# [15. 15.]
# Nível de significância: 0.05
