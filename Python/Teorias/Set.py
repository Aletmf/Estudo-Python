"""Sets são coleções não ordenadas (não contém index), e imutáveis, e não permite valores duplicados"""

"""conjuntoset = {"item1", "item2", 3, True, "são paulo"}
print(conjuntoset)
print(len(conjuntoset))"""

tupla = {3, 7, 9, 5, 8, 0, 1, 2}

for x in tupla:
    print(x)

#Maneira para acessar cada item do conjunto set ↑

conjunto = {1, 2, 3, 4, 5, 6}
conjunto.add(7)
print(conjunto)
conjunto2 = {"Lula", "Polvo"}
conjunto.update(conjunto2)
print(conjunto)

#Removendo ↓

conjunto.remove(4)
print(conjunto)

#conjunto.update, conjunto.symmetric_diference, conjunto.intersection, conjunto.intersection_update