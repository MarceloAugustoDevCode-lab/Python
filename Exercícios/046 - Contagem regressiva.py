#046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
for contador in range(10,-1,-1):
    print(contador)
    time.sleep(1)
print('\033[1;31;40mEXPLODIU\033[m')
