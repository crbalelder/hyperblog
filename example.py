
lista = [1,2,3,4,5,6]
lista_2 = []

for element in lista:
    result  = element**2 + 2*element - 1/element
    lista_2.append(result)

print(lista_2)