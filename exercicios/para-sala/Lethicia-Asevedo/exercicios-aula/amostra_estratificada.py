#Amostragem Estratificada

populacao = {
    'grupo1': [1,2,3,4,5],
    'grupo2': [6,7,8,9,10],
    'grupo3': [11.12,13,14,15]
}

tamanho_amostra_por_grupo = 2

#Amostragem Estratificada
#membro = grupo
import random
amostra_est = {grupo: random.sample(membros, tamanho_amostra_por_grupo) for grupo, membros in populacao.items()}
print(f"Amostra Estratificada: {amostra_est}")