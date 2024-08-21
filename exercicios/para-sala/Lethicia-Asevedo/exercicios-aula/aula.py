#Media 
#dados
dados = [5,7,7,8,8,8,9,10]
media = sum(dados) / len(dados)
print(f"A média é: {media}" )
print("************************************************************")
#_______________________________________________________________________________
#Mediana
#dados 
dados = [5,7,7,8,8,8,9,10]
#organizar os dados 
dados_ordenados = sorted(dados)
n = len(dados_ordenados)

if n % 2 == 1:
    mediana = dados_ordenados[n//2]
else:
    mediana = (dados_ordenados [dados_tamanho //2]+ dados_ordenados[dados_tamanho //2])

print(f"O valor da mediana é: {mediana}")
print("************************************************************")
#_______________________________________________________________________________
#Moda
#dados
dados = [5,7,7,8,8,8,9,10]

frequencia ={}
for numero in dados:
    if numero in frequencia: 
        frequencia [numero] += 1 
    else:
        frequencia[numero] = 1

max_frequencia = max(frequencia.values())
moda = [key for key, value in frequencia.items() if value == max_frequencia]
print(f"A moda é: {moda}")
print("************************************************************")
#_______________________________________________________________________________

import math
#Desvio Padrão
#dados
dados = [5,7,7,8,8,8,9,10]

#Step 1: Calcular a média 
dados = [5,7,7,8,8,8,9,10]
media = sum(dados) / len(dados)
print(media)

#Step 2: Calcular a variância
soma_quadrados_dif = sum((x - media)** 2 for x in dados)
print(soma_quadrados_dif)

variância = soma_quadrados_dif / quantidade
print(variância)

#Step 3: Calcular o desvio padrão 
desvio_padrao = math.sqrt(variância)
print(f"Desvio padrão é: {desvio_padrao:.2f}")
print("************************************************************")