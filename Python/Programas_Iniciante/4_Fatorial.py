"""
Como achar o fatorial de um número
"""

fatorial = 1

numero = int(input("Qual será o número?"))

if numero == 0:
    print("O fatorial de 0 e 1")
elif numero < 0:
    print("Não existe fatorial de numeros negativos.")
else:
    for x in range (1, numero+1): #Utiliza-se numero+1 pois na segunda condição do for ele pega (variavel-1), e como precisamos multiplicar o número digitado também, fazemos assim.
        fatorial = fatorial * x #Multiplica começando do 1 todos os números até o número digitado pelo usuário
print(f"O fatorial de {numero} é {fatorial}")
