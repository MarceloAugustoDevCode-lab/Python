

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))
tupla = (n1, n2, n3, n4)
print(f'valores digitados: {tupla}')

if 9 in tupla:
    mostre1 = tupla.count(9)
    print(f'O valor 9 apareceu {mostre1} vezes')
if 3 in tupla:
    mostre = tupla.index(3)
    print(f'O valor 3 apareceu na {mostre+1}° poasição')
else:
    print('O valor não apareceu em nenhuma posição!')

print(f'Os valores pares digitados é:', end=' ')
for numero in tupla:
    if numero % 2==0:
        pares = numero
        print(numero ,end='')
