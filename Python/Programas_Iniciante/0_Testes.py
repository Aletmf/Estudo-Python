#Area do retângulo
#Area do quadrado
#Desconto de % em produto
#Área do círculo
#Conversão de reais para dolar
#Conversão de dolar para reais

baseRetangulo = int(input("Digite o valor da base do retângulo: "))
alturaRetangulo = int(input("Digite o valor da altura do retângulo: "))
areaRetangulo = baseRetangulo * alturaRetangulo
print(areaRetangulo)


ladoQuadrado = int(input("Digite o valor do lado do quadrado: "))
areaQuadrado = ladoQuadrado * 2
print(areaQuadrado)

valorOriginal = int(input("Qual o valor original do produto? R$"))
valorDesconto = valorOriginal * 0.85
print("O valor com desconto de 15% será R${0}".format(valorDesconto))

valorDol = float(input("Qual o valor em dolares que deseja converter para real? R$"))
valorDol = valorDol * 5.65
print(valorDol)

valorReal = float(input("Qual o valor em real que deseja converter para dolar? R$"))
valorReal = valorReal/5.65
print(valorReal)