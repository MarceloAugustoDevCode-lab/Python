#028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

adivinhar = random.randint(1, 5)
print(adivinhar)# VOCÊ VER SE O NUMERO SORTEADO. para testar o codigo.
numero = int(input('tente adivinhar o numero ?'))
print('PROCESSANDO...')
time.sleep(3)
if numero == adivinhar:
    print('Parabens você venceu!')
else:
    print('Você perdeu!')