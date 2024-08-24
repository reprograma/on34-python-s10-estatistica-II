from scipy.stats import ttest_rel

antes = [30, 28, 35, 33, 40, 29, 32, 36]
depois = [25, 22, 30, 28, 35, 27, 30, 31]

r = ttest_rel(antes, depois)

significancia = 0.05

if r.pvalue < significancia:
    print("Rejeitamos a hipótese nula. Houve uma melhoria significativa no tempo de conclusão.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que houve uma melhoria significativa.")

print(f"Valor p: {r.pvalue:.5f}")
print(f"Estatística: {r.statistic:.5f}")
print(f"Nível de significância: {significancia:.2f}")

# Rejeitamos a hipótese nula. Houve uma melhoria significativa no tempo de conclusão.
# Valor p: 0.00008
# Estatística: 8.21704
# Nível de significância: 0.05
