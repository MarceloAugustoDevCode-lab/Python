#045 - Cria um programa que faça o computador jogar Jokanpô com você
from random import randint
itens =('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Sua escolha: '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida')
