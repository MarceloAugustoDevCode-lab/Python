





import pygame
import flet as ft



pygame.init()
# lembrando que as barras tem que ser invertidas "F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3".
# crie uma pasta na pasta principal ou em qualquer pasta do pc e coloque o caminho.
pygame.mixer.music.load(r"F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3")
# "a musica e essa foi que eu comecei a gosta de infomatica."

play = ""
pause = ""
stop = ""
while play != 'stop':
    play = input("Digite o \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")

    if play == 'play':
        pygame.mixer.music.play()
    elif play == 'pause':
        pygame.mixer.music.pause()
    elif play == 'stop':
        pygame.mixer.music.stop()
    else:
        print("Opção inválida. Tente novamente.")