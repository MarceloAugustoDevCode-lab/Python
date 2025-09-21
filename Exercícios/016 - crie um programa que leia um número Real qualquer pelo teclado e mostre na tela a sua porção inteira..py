#016 - crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#exemplo: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite o numero: '))
inteiro = math.trunc(num)
print('O numero de porção intera é {}'.format(inteiro))


