#038 - Escreva um programa que leia dois números inteiros a compare-os. mostrando na tala uma mensagem:
# O primeiro valor é maior O segundo valor é maior Não existe valor maior, os dois são iguais

numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero > numero2:
    print('O primeiro e maior \033[1;31;40m{}\033[m'.format(numero))
elif numero2 < numero:
    print('O segundo e maior \033[1;31;40m{}\033[m'.format(numero))
else:
    print('O primeiro igual ao segundo \033[1;31;40m{}\033[m'.format(numero))
