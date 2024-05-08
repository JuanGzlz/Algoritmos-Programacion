lista = [2,4,6,8]
lista2 = lista[:]
lista3 = []

lista2.reverse()

for i in range(0, len(lista)):
    total = 0
    for j in range(i, len(lista)):
        total += lista[j]
    lista[i] = total


print(lista)

for i in range(0, len(lista2)):
    total = 0
    for j in range(i, len(lista2)):
        total += lista2[j]
    lista2[i] = total

print(lista2)

for i in range(0, len(lista)):
    for j in range(0, len(lista2)):
        if i == j:
            print(lista2[j] - lista[i])
            lista3.append(abs(lista2[j] - lista[i]))

print(lista3)
