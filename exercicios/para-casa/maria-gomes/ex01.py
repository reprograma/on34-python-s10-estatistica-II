from scipy.stats import ttest_1samp

calorias = [1900, 2100, 2050, 1980, 1950, 2100, 2000, 2150, 2200, 1850, 1990, 1950, 2050, 2080, 2100,
            1900, 1950, 2050, 2150, 2000, 2200, 1900, 2100, 2000, 2150, 1850, 1990, 1950, 2050, 2080]

r = ttest_1samp(calorias, 2000)

significancia = 0.05

if r.pvalue < significancia:
    print("Rejeitamos a hipótese nula. A média de calorias é diferente de 2000.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que a média de calorias é diferente de 2000.")

print(f"Valor p: {r.pvalue:.5f}")
print(f"Estatística: {r.statistic:.5f}")
print(f"Nível de significância: {significancia:.2f}")

# Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que a média de calorias é diferente de 2000.
# Valor p: 0.16039
# Estatística: 1.44068
# Nível de significância: 0.05
