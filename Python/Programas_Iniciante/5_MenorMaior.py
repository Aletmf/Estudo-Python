#Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o resultado

CONSTANTE_NUMEROS = 5
menorNumero = 500000
maiorNumero = -1

numeros = [0] * CONSTANTE_NUMEROS

print(35 * "-")
print("PROGRAMA PARA VERIFICAR MAIOR E MENOR NÚMERO DA SEQUÊNCIA DIGITADA")
print(35 * "-")
for x in range(CONSTANTE_NUMEROS):
    numeros[x] = float(input(f"\nDigite o número {x}: "))

for x in range(CONSTANTE_NUMEROS):
    if numeros[x] > maiorNumero:
        maiorNumero = numeros[x]
    if numeros[x] < menorNumero:
        menorNumero = numeros[x]
print(f"O maior número é {maiorNumero} e o menor número é {menorNumero}")