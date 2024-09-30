import pandas as pd

tabela = pd.read_excel("C:\\Users\\super\\OneDrive\\Área de Trabalho\\Produtos.xlsx")
print(tabela)

tabela.loc[tabela["Tipo"] == "Serviço","Multiplicador Imposto"] = 1.5

tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Multiplicador Imposto"]
print(tabela)

tabela.to_excel("ProdutosPandas.xlsx", index = False)