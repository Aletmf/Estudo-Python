"""
Crie um programa que armazene informações sobre livros em uma biblioteca. Para cada livro, o dicionário deve conter as seguintes informações:
Título
Autor
Ano de publicação
Gênero
Status (se está disponível ou emprestado)

O programa deve permitir que o usuário:

Adicione um livro à biblioteca.
Consulte os detalhes de um livro pelo título.
Liste todos os livros que estão disponíveis.
Modifique o status de um livro para "emprestado" ou "disponível".
Remova um livro da biblioteca.
"""
import os

#Variaveis para armazenar dados dos livros
biblioteca = {}
titulo = ""
nomeAutor = ""
anoPublicacao = ""
genero = ""
status = ""


def obterDados():
    titulo = input("Digite o título do livro: ")
    nomeAutor = input("\nDigite o nome do autor: ")
    anoPublicacao = input("\nDigite o ano de publicação: ")
    genero = input("\nDigite o gênero do livro: ")
    status = input("\nDigite o status de disponibildiade do livro (emprestado/disponível): ")
    status = status.upper()

    return titulo, nomeAutor, anoPublicacao, genero, status

def inserirDicionario():
    titulo, nomeAutor, anoPublicacao, genero, status = obterDados()
    print(titulo)
    print(nomeAutor)
    print(anoPublicacao)
    print(genero)
    print(status)

    biblioteca[titulo] = {
        "Autor": nomeAutor,
        "Ano de publicacao": anoPublicacao,
        "Genero": genero,
        "Status": status
    }

def mostrarNomes(biblioteca):
    index = 1
    for x in biblioteca.keys():
        print(f"{index}- {x}")
        index += 1

def consultarLivro(biblioteca):
    mostrarNomes(biblioteca)
    nomeDesejado = input("Digite o nome do livro a ser consultado: ")
    for percorre in biblioteca:
        if (percorre.upper() == nomeDesejado.upper()):
            print(biblioteca[percorre])
    input("Pressione qualquer tecla para continuar...")

def mostrarLivrosDisp(biblioteca):
    for titulo, dados in biblioteca.items():
        if dados["Status"] == "DISPONIVEL":
            print(f"Título: {titulo}\nNome do autor: {dados["Autor"]}\nPublicação: {dados["Ano de publicacao"]}\nGenero: {dados["Genero"]}\nStatus: {dados["Status"]}\n")
    input("Pressione qualquer tecla para continuar...")
             
def modificaStatus(biblioteca):
    mostrarNomes(biblioteca)
    livroAlterar = input("\nDigite o nome do livro a ter o status alterado: ")

    for titulo, dados in biblioteca.items():
        if(titulo.upper() == livroAlterar.upper()):
            if dados["Status"] == "DISPONIVEL":
                dados["Status"] = "EMPRESTADO"
            else:
                dados["Status"] = "DISPONIVEL"
            print("STATUS ALTERADO!\n")
            print(titulo, biblioteca[titulo])
    input("Pressione qualquer tecla para continuar...")
    
def removerLivro(biblioteca):
    mostrarNomes(biblioteca)
    removedor = input("Digite o nome do livro a ser removido: ")
    biblioteca.pop(removedor)


def menu():
    Menu = ""
    opInserir = ""
    opRemove = ""
    while Menu != 6:
        print("Menu de opções!!\n\n")
        Menu = int(input("Digite a opção desejada: \n\n1- Adicionar livro\n2- Consultar livro\n3- Lista dos livros disponíveis\n4- Modificar status livro\n5- Remover livro\n6- Sair\n\n-> "))
        match Menu:
            case 1:
                while opInserir != 0:
                    inserirDicionario()
                    opInserir = int(input("Deseja inserir outro livro?\n1- SIM\n0- NÃO\n\n-> "))
            case 2:
                consultarLivro(biblioteca)
            case 3:
                mostrarLivrosDisp(biblioteca)
            case 4:
                modificaStatus(biblioteca)
            case 5:
                while opRemove != 0:
                    removerLivro(biblioteca)
                    opRemove = int(input("Deseja remover outro livro?\n1- SIM\n0- NÃO\n\n-> "))
            case 6:
                  break
            case _:
                  print("Opção inválida")


menu()


