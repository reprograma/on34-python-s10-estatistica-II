#importar biblioteca 
import random

#dados 
#range=intervalo

populacao = list(range(1,101))#Vai me trazer uma lista de números aleatórios do 1 ao 100
print(f"População: {populacao}")

tamanho_amostra = 10
print(f"Tamanho da amostra: {tamanho_amostra}")

#Amostra aleatória simples
# Sample : Seleciona números sem repeti-los 
amostra = random.sample(populacao, tamanho_amostra)
print(f"Amostra Aleatória Simples: {amostra}")