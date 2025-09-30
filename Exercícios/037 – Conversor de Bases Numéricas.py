#037 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera´a base de conversão
#1 para binario
#2 para octal
#3 para hexadecimal

numero = int(input('Digite o numero: '))
escolha = input('Digite o escolha ').split()

if escolha == '1':
    binario = bin(numero)
    print(binario)
    print('\033[1;32;40m{}\033[m'.format(binario))
elif escolha == '2':
    octal = oct(numero)
    print('\033[1;32;40m{}\033[m'.format(octal))
elif escolha == '3':
    hexadecimal = hex(numero)
    print('\033[1;32;40m{}\033[m'.format(hexadecimal))
else:
    pass
