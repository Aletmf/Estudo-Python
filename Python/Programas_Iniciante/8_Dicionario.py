"""
Crie um programa que funcione como um pequeno sistema de cadastro de estudantes utilizando dicionários.
Cada estudante deve ter: Nome, Idade, Nota final

Permitir que o usuário cadastre informações de vários estudantes.
Após cadastrar os estudantes, exiba uma lista com todos eles e suas respectivas informações.

Criar o dicionário vazio:

O dicionário terá como chave o nome do estudante e como valor outro dicionário com a idade e a nota final.
Adicionar funcionalidade:

Peça ao usuário para inserir o nome, a idade e a nota de cada estudante. OK
Armazene essas informações no dicionário.
Exibir os dados: 

Após terminar os cadastros, exiba todos os estudantes com suas respectivas informações. OK
(Desafio extra):
Calcule e exiba a média das notas de todos os estudantes cadastrados.
"""

def obterDados():
    nome = input("\nDigite o nome do estudante: ")
    idade = int(input("\nDigite a idade do aluno: "))
    notaFinal = float(input("\nDigite a nota final do aluno: "))
    return nome, idade, notaFinal




estudantes = {}
somador = 0
contador = 0
op = 3
print("Sistema para cadastro de alunos!\n")

while op != 0:
    nome, idade, notaFinal = obterDados()
    estudantes[nome] = {"idade": idade, "notaFinal": notaFinal}
    op = int(input("Deseja incluir mais algum aluno?\n\n1- SIM\n0- NÃO\n\n-> "))

print(estudantes.items())

teste = estudantes.values()

for x in teste:
    somador = somador + x["notaFinal"]
    contador+= 1



media = somador/contador
"{:.2f}".format(media)
print("Média: ", media)

