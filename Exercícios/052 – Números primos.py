#052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite o numero: '))
tot= 0
for c in range(1,numero+1):
    if numero % c == 0:
        print('\033[1;31;40m', end='')
        tot+= 1
    else:
        print('\033[1;34;40m', end='')
    print(f'{c}\033[m',end=' ')
print(f'\nO numero {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')

