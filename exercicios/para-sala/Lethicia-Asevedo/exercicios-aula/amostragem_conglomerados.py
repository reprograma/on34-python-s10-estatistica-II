#Amostragem por Conglomerados 

#dados
populacao = {
    'conglomerado1' : [1,2,3,4,5],
    'conglomerado2' : [6,7,8,9,10],
    'conglomerado3' : [11,12,13,14,15],
    'conglomerado4' : [16,17,18,19,20]
}
print(populacao)
num_conglomerados_selecionados = 2

#Amostra por conglomerados

import random
#keys = as chaves do dicionário
conglomerados = list(populacao.keys())
conglomerados_selecionados = random.sample(conglomerados, num_conglomerados_selecionados)
amostra = {conglomerado: populacao[conglomerado] for conglomerado in conglomerados_selecionados}
print(f"Amostra de conglomerados: {amostra}")

