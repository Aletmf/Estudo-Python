#MiniGame Acertar número
numero = 8
palpite = 0

while True: #Fazemos dessa maneira para primeiro perguntar e depois verificar. Condição será sempre verdadeira
    palpite = int(input("Qual seu palpite para o número?\n-> "))
    if palpite == numero: #Verificação aqui
        print("Você acertou!")
        break #Interrupção caso acerte
    else:
        print("Você errou")
