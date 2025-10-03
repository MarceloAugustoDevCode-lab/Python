





import pygame
import flet as ft
import os


pygame.init()
# lembrando que as barras tem que ser invertidas "F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3".
# crie uma pasta na pasta principal ou em qualquer pasta do pc e coloque o caminho.

# "a musica e essa foi que eu comecei a gosta de Informatica."
# pygame.mixer.music.load(r"F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3")
arquivos = os.path.join(r"F:\01 Programas Dev\Estudos\Python\som")
# lista de nomes musicas mp3.
arqmp3 = os.listdir(arquivos)
lista = list(arqmp3)
cont = 0
for c in range(0, len(lista)):
    totalcaminho = arquivos + "\\" + lista[c]
    print(totalcaminho)
totalcaminho = arquivos + "\\" + lista[c]

pygame.mixer_music.load(totalcaminho)
play = input("Digite o \033[1;31;40m'<'\033[m para voltar  \033[1;31;40m'>'\033[m para avançar")
if play == '<':
    c -= 1
    pygame.mixer.music.play()
elif play == '>':
    c += 1
    pygame.mixer.music.play()


play = ''
pause = ''
stop = ''
retroceder = ''
proxima = ''

while play != 'stop':
    play = input("Digite o \033[1;31;40m'<'\033[m para voltar \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'>'\033[m para avançar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")
    musica = c
    if play == 'play':
        pygame.mixer.music.play()
    elif play == 'pause':
        pygame.mixer.music.stop()
    elif play == 'stop':
        pygame.mixer.music.stop()
    else:
        print("Opção inválida. Tente novamente.")