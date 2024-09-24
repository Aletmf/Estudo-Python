#Programa para descobrir se um número é primo

numero = 0
logico = True

opcao = input("Deseja verificar numeros primos?\nS - SIM\nN - NÃO\n-> ")
opcao = opcao.capitalize()

while opcao != 'N':
    numero = int(input("Digite o número desejado: "))
    if numero == 0: print("0 não é primo.")
    elif numero == 1: print("0 não é primo.")
    else:
        for x in range(2,numero):
            if numero%x == 0:
                logico = False
                break
            else: logico = True
    if logico:
        print("Seu número é primo")
    else: print("Seu número não é primo")

    opcao = input("Deseja verificar mais números?\nS - SIM\nN - NÃO\n-> ")
    opcao = opcao.capitalize()