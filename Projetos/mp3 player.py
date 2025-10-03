import pygame
import os

# Inicializa o pygame e seus módulos
pygame.init()

# Lembrando que as barras tem que ser invertidas "F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3".
# crie uma pasta na pasta principal ou em qualquer pasta do pc e coloque o caminho.
# " Essa música que foi que comecei a gostar de Informatica."
# pygame.mixer.music.load(r"F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3")

# Caminho da pasta onde estão as músicas
arquivos = os.path.join(r"F:\01 Programas Dev\Estudos\Python\som")


# lista de nomes musicas mp3.
arqmp3 = os.listdir(arquivos)


# Lista de arquivos dentro da pasta
lista = list(arqmp3)

for numero in range(0, len(lista)):
    musica = arquivos + "\\" + lista[numero]
    print(numero,end=' ')
    print(musica)
pygame.mixer_music.load(musica)
print(numero)


play = ''
pause = ''
stop = ''
retroceder = ''
proxima = ''

while play != 'stop':
    play = input("Digite o \033[1;31;40m'<'\033[m para voltar \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'>'\033[m para avançar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")
    musica = 0
    if play == 'play':
        pygame.mixer.music.play()
    elif play == 'pause':
        pygame.mixer.music.stop()
    elif play == 'stop':
        pygame.mixer.music.stop()
    elif play == '<':
        pygame.mixer_music.load()
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        print()
    elif play == '>':
        pygame.mixer_music.load()
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        print()
    else:
        print("Opção inválida. Tente novamente.")