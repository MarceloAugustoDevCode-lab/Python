#045 - Cria um programa que faça o computador jogar Jokanpô com você

jogador1 = str(input('Digite o nome do jogador 1: '))
jogador2 = str(input('Digite o nome do jogador 2: '))


escolhajogador1 = str(input('Digite a sua escolha do jogador {} ?'.format(jogador1)))
if escolhajogador1 == 'pedra' or escolhajogador1 == 'papel' or escolhajogador1 == 'tesoura':
    if escolhajogador1 == 'pedra':
        sobra = 'papel' and 'tesoura'
        print('O jogador {} escolheu pedra'.format(jogador1))
    elif escolhajogador1 == 'papel':
        sobra = 'tesoura' and 'pedra'
        print('O jogador {} escolheu papel'.format(jogador1))
    else:
        sobra = 'pedra' and 'papel'
        print('O jogador {} escolheu tesoura'.format(jogador1))


escolhajogador2 = str(input('Digite a sua escolha do jogador {} ?'.format(jogador2)))
if escolhajogador2 == 'pedra' or escolhajogador2 == 'papel' or escolhajogador2 == 'tesoura':
    if escolhajogador2 == 'pedra':
        sobra = 'papel' and 'tesoura'
        print('O jogador {} escolheu pedra'.format(jogador2))
        if escolhajogador1 == 'papel':
            print('O jogador {} Perdeu!, pois papel embrulha pedra'.format(jogador2))
        elif escolhajogador1 == 'tesoura':
            print('O jogador {} Venceu!, pois pedra quebra tesoura'.format(jogador2))
        else:
            pass
    elif escolhajogador2 == 'papel':
        sobra = 'tesoura' and 'pedra'
        print('O jogador {} escolheu papel'.format(jogador2))
        if escolhajogador1 == 'papel':
            print('O jogador {} Venceu!, pois papel embrulha pedra'.format(jogador2))
        elif escolhajogador1 == 'tesoura':
            print('O jogador {} Venceu!, pois tesoura corta papel'.format(jogador2))
        else:
            pass
    else:
        sobra = 'pedra' and 'papel'
        print('O jogador {} escolheu tesoura'.format(jogador2))
        if escolhajogador1 == 'papel':
            print('O jogador {} Venceu!, pois pois tesoura corta papel'.format(jogador2))
        elif escolhajogador1 == 'tesoura':
            print('O jogador {} Perdeu! pois pedra quebra tesoura'.format(jogador2))
        else:
            pass





