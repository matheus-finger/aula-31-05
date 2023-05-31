lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)
# a soma de listas é uma função do objeto lista
print(lista1.__add__(lista2))
# ps.: funções também são objetos no python

# forma diferente de criar uma lista
x = list({1, 2, 3, 4, 5})
# mesma coisa de: x = list.__init__({1, 2, 3, 4, 5})
print(x)

x.append(10)
# engual a
list.append(x, 10)