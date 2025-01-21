"""Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])"""

import numpy as np

matriz = np.array([[3,4,1],
                   [3,1,5]])

somador = 0

for i in range(matriz.shape[0]): #Matriz.shape retorna a quantidade de linhas e depois colunas. exemplo (2,3). Então, se chamarmos o 2 de i e o 3 de j conseguimos acessar
    print(matriz[i]) #Matriz no índice "i", pois se fizessemos print apenas do "i" ele apenas printaria 0 e 1, pois incrementou no proprio i (iniciado em zero) com base no shape
    # ↑ percorre as linhas
    for j in range(matriz.shape[1]): #Percorre as colunas
        print(matriz[i][j]) #Combinação dos dois para mostrar um por um
        somador = somador + matriz[i][j]

print(somador)