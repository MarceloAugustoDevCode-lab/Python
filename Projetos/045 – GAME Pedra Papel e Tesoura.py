#045 - Cria um programa que faça o computador jogar Jokanpô com você

jogador1 = str(input('\033[1;31;40mDigite o nome do jogador 1: \033[m'))
jogador2 = str(input('\033[1;32;40mDigite o nome do jogador 2: \033[m'))


escolhajogador1 = str(input('Digite a sua escolha do \033[1;31;40mjogador {}\033[m ?'.format(jogador1)))
if escolhajogador1 == 'pedra' or escolhajogador1 == 'papel' or escolhajogador1 == 'tesoura':
    if escolhajogador1 == 'pedra':
        sobra = 'papel' and 'tesoura'
        print('O jogador {} escolheu \033[1;31;40m pedra\033[m'.format(jogador1))
    elif escolhajogador1 == 'papel':
        sobra = 'tesoura' and 'pedra'
        print('O jogador {} escolheu \033[1;31;40m papel\033[m'.format(jogador1))
    else:
        sobra = 'pedra' and 'papel'
        print('O jogador {} escolheu \033[1;31;40m tesoura\033[m'.format(jogador1))


escolhajogador2 = str(input('Digite a sua escolha do \033[1;32;40mjogador {}\033[m ?'.format(jogador2)))
if escolhajogador2 == 'pedra' or escolhajogador2 == 'papel' or escolhajogador2 == 'tesoura':
    if escolhajogador2 == 'pedra':
        sobra = 'papel' and 'tesoura'
        print('O jogador {} escolheu \033[1;32;40m pedra\033[m'.format(jogador2))
        if escolhajogador1 == 'papel':
            print('O jogador {} Perdeu!, pois papel embrulha pedra'.format(jogador2))
        elif escolhajogador1 == 'tesoura':
            print('O jogador {} Venceu!, pois pedra quebra tesoura'.format(jogador2))
        else:
            pass
    elif escolhajogador2 == 'papel':
        sobra = 'tesoura' and 'pedra'
        print('O jogador {} escolheu \033[1;32;40m papel\033[m'.format(jogador2))
        if escolhajogador1 == 'pedra':
            print('O jogador {} Venceu!, pois papel embrulha pedra'.format(jogador2))
        elif escolhajogador1 == 'tesoura':
            print('O jogador {} perdeu!, pois tesoura corta papel'.format(jogador2))
        else:
            pass
    else:
        sobra = 'pedra' and 'papel'
        print('O jogador {} escolheu \033[1;32;40m tesoura\033[m'.format(jogador2))
        if escolhajogador1 == 'papel':
            print('O jogador {} Venceu!, pois pois tesoura corta papel'.format(jogador2))
        elif escolhajogador1 == 'pedra':
            print('O jogador {} Perdeu! pois pedra quebra tesoura'.format(jogador2))
        else:
            pass





