lista = ["carro", "barco", "aviao"]
print(lista)

lista.insert(1, "bicicleta") #Insere no elemento 1. .insert(index a ser inserido, valor a ser inserido)
lista.extend(["bicicleta", "navio"])
print(lista)
 
"""lista.append(["moto", "jetski", "bicicleta", "boing"])
print(lista)
for x in range(len(lista)):
    print(x, lista[x])
"""
texto = "meunome@gmail.com"

lista2 = list(texto)
print (lista2)

texto = texto.split('@')
print(texto)

#Adicionar/Remover elementos

#lista.pop(0) #Remove (pop), semelhante ao C, o elemento do index determinado dentro dos parenteses ().
#lista.remove('bicicleta')

#del lista - Comando deleta a lista
#del lista[1] - Comando apaga o elemento localizado no index 1 da lista
#lista.clear() - Limpa todos elementos da lista, mas deixando ela na memória. Diferente do delete, que some com tudo dela
print(lista)

lista.sort() #Ordena do menor para o maior. Seja a lista composta por palavras ou números.
lista.sort(reverse = True) #Ordena de forma decrescente, do maior para o menor, seja a lista composta por palavras ou números.
lista.reverse #Apenas inverte a lista.
lista.sort(key = str.lower) #Trata os elementos como se estivessem todos em letra minúscula, e depois ordena.
lista = lista2.copy() #Serve para copiar os elementos da lista 2 na lista 1

for x in range(len(lista)):
    print(x)