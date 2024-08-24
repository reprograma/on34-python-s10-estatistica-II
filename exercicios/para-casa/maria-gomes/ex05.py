from scipy.stats import f_oneway

fertilizante_a = [20, 22, 19, 21, 20]
fertilizante_b = [18, 20, 17, 19, 18]
fertilizante_c = [25, 27, 26, 28, 26]

r = f_oneway(fertilizante_a, fertilizante_b, fertilizante_c)

significancia = 0.05

if r.pvalue < significancia:
    print("Rejeitamos a hipótese nula. Pelo menos uma das médias dos crescimentos das plantas é diferente.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências suficientes para afirmar que as médias dos crescimentos das plantas são diferentes.")

print(f"Valor p: {r.pvalue:.5f}")
print(f"Estatística: {r.statistic:.5f}")
print(f"Nível de significância: {significancia:.2f}")

# Rejeitamos a hipótese nula. Pelo menos uma das médias dos crescimentos das plantas é diferente.
# Valor p: 0.00000
# Estatística: 66.66667
# Nível de significância: 0.05
