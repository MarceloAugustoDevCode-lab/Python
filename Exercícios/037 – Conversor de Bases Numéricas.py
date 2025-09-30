#037 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera´a base de conversão
#1 para binario
#2 para octal
#3 para hexadecimal
'''
numero = int(input('Digite o numero: '))
escolha = input('Digite o escolha \033[1;31;40mA\033[m para \033[1;31;40mBinario\033[m, \033[1;35;40mB\033[m para'
                ' \033[1;35;40mOctal\033[m, \033[1;32;40mC\033[m para \033[1;32;40mHexadecimal\033[m.').upper()

if escolha == 'A':
    binario = bin(numero)
    print('\033[1;32;40m{}\033[m'.format(binario))
elif escolha == 'B':
    octal = oct(numero)
    print('\033[1;32;40m{}\033[m'.format(octal))
elif escolha == 'C':
    hexadecimal = hex(numero)
    print('\033[1;32;40m{}\033[m'.format(hexadecimal))
else:
    pass
'''
#OU

num = int(input('Digite o numero: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcão = int(input('Sua opção: '))

if opcão == 1:
    num = bin(num)
    print('\033[1;31;40m{}\033[m'.format(num[2:]))
elif opcão == 2:
    num =  oct(num)
    print('\033[1;35;40m{}\033[m'.format(num[2:]))
elif opcão == 3:
    num = hex(num)
    print('\033[1;32;40m{}\033[m'.format(num[2:]))
else:
    print('Opção invalida!')