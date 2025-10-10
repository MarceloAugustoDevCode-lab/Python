# 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

venceu = 0
while True:
    computador = random.randint(1,10)
    print(30 * '-')
    print('Jogando...')
    print(30 * '-')
    print(computador)
    jogador = int(input('Digite um valor: '))
    esccolha = str(input('Escolha se é Par ou Ímpar: [p para par/ i para impar]:  ')).strip().upper()[0]
    pares = (jogador + computador) % 2
    #print(pares)
    total = jogador + computador
    if pares == 0 and esccolha == 'P':
        print(30*'-')
        print(f'Você Venceu!, Você jogou {jogador} e o computador {computador}. Total deu {total} deu Par')
        venceu += 1
    elif pares == 1 and esccolha == 'I':
        print(30 * '-')
        print(f'Você Venceu!, Você jogou {jogador} e o computador {computador}. Total deu {total} deu Ímpar')
        venceu += 1
    else:
        print(30 * '-')
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {venceu} vezes.')
