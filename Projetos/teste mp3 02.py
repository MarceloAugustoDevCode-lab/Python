import pygame
import os
import flet as ft

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





def main(page: ft.Page):
    page.title = "Icon button with 'click' event"

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked, data=0
    )
    t = ft.Text()

    page.add(b, t)








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

    ft.app(main)