#Projeto gerador de senhas

chave = input("Digite a base da sua senha: ")
senha = ""

for letra in chave:
    if letra in "Aa": senha = senha + "3"
    elif letra in "Bb": senha = senha + "¨"
    elif letra in "Cc": senha = senha + "&"
    elif letra in "Dd": senha = senha + "0"
    elif letra in "Ee": senha = senha + "2"
    elif letra in "Ff": senha = senha + "5"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Oo": senha = senha + "*"
    else: senha = senha + letra

    
print(senha)