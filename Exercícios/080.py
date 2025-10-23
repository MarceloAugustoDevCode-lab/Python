

lista = []

n = int(input('Digite um valor: '))
lista.append(n)


if n > 4 in lista:
    lista.insert(3,n)

print(lista)