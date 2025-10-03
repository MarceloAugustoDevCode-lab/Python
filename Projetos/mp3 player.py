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

# Mostra as músicas numeradas
for i, nome in enumerate(lista):
    print(i, arquivos + "\\" + nome)

# Seleciona a primeira música (índice 0)
musica = arquivos + "\\" + lista[0]
pygame.mixer.music.load(musica)


play = ''
pause = ''
stop = ''
retroceder = ''
proxima = ''

while play != 'stop':
    play = input("Digite o \033[1;31;40m'<'\033[m para voltar \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'>'\033[m para avançar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")

    if play == 'play':
        pygame.mixer.music.play()
    elif play == 'pause':
        pygame.mixer.music.stop()
    elif play == 'stop':
        pygame.mixer.music.stop()
    elif play == '<':
        musica = arquivos + "\\" + lista[0]
        print(musica)
        pygame.mixer.music.load(musica)
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
    elif play == '>':
        musica = arquivos + "\\" + lista[+1]
        print(musica)
        pygame.mixer.music.load(musica)
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
    else:
        print("Opção inválida. Tente novamente.")