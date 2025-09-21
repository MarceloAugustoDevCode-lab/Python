#016 - crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#exemplo: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite o numero: '))
inteiro = math.trunc(num)
print('O numero digitado é {} de porção intera é {}'.format(num,inteiro))

#ou

#só a Função trunc que foi importada em vez colocar a variavel coloquei no print direto.
from math import trunc
num2 = float(input('Digite o numero: '))
print('O numero digitado é {} de porção intera é {}'.format(num2,math.trunc(num2)))