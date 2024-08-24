from scipy.stats import ttest_ind

turma_a = [85, 78, 90, 88, 76, 95, 89, 84]
turma_b = [82, 75, 85, 80, 79, 88, 83, 77]

r = ttest_ind(turma_a, turma_b)

significancia = 0.05

if r.pvalue < significancia:
    print("Rejeitamos a hipótese nula. Há uma diferença significativa entre as médias das duas turmas.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que há uma diferença significativa entre as médias das duas turmas.")

print(f"Valor p: {r.pvalue:.5f}")
print(f"Estatística: {r.statistic:.5f}")
print(f"Nível de significância: {significancia:.2f}")

# Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que há uma diferença significativa entre as médias das duas turmas.
# Valor p: 0.11635
# Estatística: 1.67384
# Nível de significância: 0.05
