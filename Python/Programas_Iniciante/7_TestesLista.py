"""
Crie uma lista chamada numeros com os valores [10, 20, 30, 40, 50].
Use as funções de lista para:
Verificar o tamanho da lista (len).
Encontrar o maior valor (max) e o menor valor (min) na lista.
Calcular a soma de todos os elementos (sum).
"""
def menu():
    saida = 3
    while saida != 0:
        print
        op = int(input("Digite a opção desejada:\n\n1 - Verificar o tamanho da lista\n2 - Encontrar o maior valor da lista\n3 - Encontrar o menor valor da lista\n4 - Calcular a soma de todos elementos\n\n-> "))
        executa_op_menu(op)
        saida = int(input("Deseja executar outra funcionalidade?\n1 - SIM\n0 - NÃO\n\n-> "))

def executa_op_menu(op):
    if(op == 1):
        print(len(lista))
    elif(op == 2):
        print(max(lista))
    elif(op == 3):
        print(min(lista))
    else:
        soma = 0
        for percorrer in lista:
            soma = soma + percorrer
        print(soma)   

def inserir_lista(numero):
    lista.append(numero)



tamanholista = int(input("Quantos números inteiros deseja incluir na lista?\n-> "))
lista = [0] * tamanholista

for x in range(0, tamanholista):
    numero = int(input("Digite o número a ser inserido na lista: "))
    inserir_lista(numero)

menu()



