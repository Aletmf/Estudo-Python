import mysql.connector
import os

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= 'Alessandro1408!',
    database='bd_casa',
)

cursor = conexao.cursor()

def adicionar_produtos(conexao, cursor):
    continuar = 3
    while continuar != 0:
        opcateg = int(input("CATEGORIA: \n\n1- Alimentação\n2- Limpeza\n3- Higiene Pessoal\n\n-> "))
        if opcateg == 1:
            categoria = "Alimentação"
        elif opcateg == 2:
            categoria = "Limpeza"
        else:
            categoria = "Higiene Pessoal"
        print(categoria)
        nome = input("\nDigite o nome do produto: ")
        nome = nome.upper()
        quantidade = int(input(f"\nDigite a quantidade de {nome} a ser adicionado: "))
        status = "Novo"
        #CREATE ↓
        inserir = f'INSERT INTO produtos (Categoria, Nome, Quantidade, Status) VALUES ("{categoria}", "{nome}", "{quantidade}", "{status}")'
        cursor.execute(inserir)
        conexao.commit()
        os.system("cls")
        continuar = int(input("Deseja inserir mais produtos?\n\n1- SIM\n0- NÃO\n\n-> "))

def read_simples(cursor):
    tabela = f'SELECT * FROM produtos'
    cursor.execute(tabela)
    resultado = cursor.fetchall()
    resultado = list(resultado)
    
    return resultado

def mostrar_estoque(cursor):
    alimentacao = []
    limpeza = []
    higieneP = []
    mostra_categoria = ""
    #READ
    resultado = read_simples(cursor)
    for x in resultado:
        if(x[0] == "Alimentação"):
            alimentacao.append(x)
        elif(x[0] == "Limpeza"):
            limpeza.append(x)
        else:
            higieneP.append(x)
    while(mostra_categoria != 5):
        mostra_categoria = int(input("Digite a categoria a ser mostrada:\n1- Alimentação\n2- Limpeza\n3- Higiene Pessoal\n4- Todos\n5- Sair\n\n-> "))
        if (mostra_categoria == 1):
            print(alimentacao)
        elif(mostra_categoria == 2):
            print(limpeza)
        elif(mostra_categoria == 3):
            print(higieneP)
        elif(mostra_categoria == 4):
            print(alimentacao, limpeza, higieneP)
        else:
            print("Saiu")
    
def alterar_info(conexao, cursor):
    resultado = read_simples(cursor)
    print(resultado)
    produto_alterado = input("\nDigite o nome do produto a ser alterado: ")
    produto_alterado = produto_alterado.upper()
    op_alterar = int(input("Digite o número da informação a ser alterada:\n\n1- Quantidade\n2- Status\n\n-> "))
    if (op_alterar == 1):
        item_alterado = "Quantidade"
        nova_quant = int(input("\nDigite a nova quantidade do produto: "))
    else:
        item_alterado = "Status"
        num_novo_status = int(input("Digite o número para o novo status do produto: \n\n1- Cheio\n2- Metade\n3- Menos da metade\n4- Vazio\n5- Outro (digitar)\n\n-> "))
        if(num_novo_status ==1):
            novo_status = "Cheio"
        elif(num_novo_status == 2):
            novo_status = "Metade"
        elif(num_novo_status == 3):
            novo_status = "Menos da metade"
        elif(num_novo_status == 4):
            novo_status = "Vazio"
        else:
            novo_status = input("\nDigite o novo status: ")

    #UPDATE
    if(op_alterar == 1):
        comando = f'UPDATE produtos SET {item_alterado} = {nova_quant} WHERE Nome = "{produto_alterado}"'
        cursor.execute(comando)
        conexao.commit()
        print("Quantidade alterada com sucesso.")
    else:
        comando = f'UPDATE produtos SET {item_alterado} = "{novo_status}" WHERE Nome = "{produto_alterado}"'
        cursor.execute(comando)
        conexao.commit()
        print("Status alterado com sucesso.")
    
def remover_produto(conexao, cursor):
    op = ""
    while (op != 2):
        resultado = read_simples(cursor)
        print(resultado)
        if(resultado == []):
            print("Lista vazia")
            return menu(conexao, cursor)
        nome_produto = input("\nDigite o nome do produto a ser removido: ").upper()
        comando = f'DELETE from produtos WHERE nome = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        print(f"\n{nome_produto} foi removido da lista. Lista atualizada: \n")
        os.system("pause")
        if(resultado == []):
            print("Lista vazia")
            return menu(conexao, cursor)
        resultado = read_simples(cursor)
        print(resultado)
        os.system("cls")
        int(input("Deseja remover mais mais algum número?\n1- SIM\n2- NÃO\n\n-> "))

def menu(conexao, cursor):
    Menu = ""
    while Menu!=4:
        Menu = int(input("Digite o número da função que deseja acessar: \n\n1- Adicionar produtos\n2- Alterar quantidade/status\n3- Mostrar Estoque\n4- Apagar produto\n5- Sair\n\n-> "))
        match Menu:
            case 1:
                adicionar_produtos(conexao, cursor)
            case 2:
                alterar_info(conexao, cursor)
            case 3:
                mostrar_estoque(cursor)
            case 4:
                remover_produto(conexao, cursor)
            case 5:
                break
    return("Menu finalizado.")

menu(conexao, cursor)

cursor.close()
conexao.close()