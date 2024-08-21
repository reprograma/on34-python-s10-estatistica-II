#importar 
from scipy.stats import ttest_1samp

#Teste t Student

#dados
dados = [22, 21, 24, 25, 20, 23, 20, 21, 23]

#Teste de hipóteses 
#HO: A média é igual a 20
#H1: A média é diferente de 20

t_statistico, p_valor = ttest_1samp(dados, 20)

print(f"Estatística t é : {t_statistico:.2f}")
print(f"Valor p é: {p_valor:.2f}")
