#Amostragem Sistemática 

#dados
import random
#range = intervalo 
populacao = list(range(1,101))
print(populacao)
intervalo = 5
ponto_de_partida = random.randint(0, intervalo -1) #randint - para embaralhar os valores
print(ponto_de_partida)

#Amostragem Sitemática 
amostra = [populacao[i] for i in range (ponto_de_partida, len(populacao), intervalo)]
print(f"Amostra sistemática: {amostra}")