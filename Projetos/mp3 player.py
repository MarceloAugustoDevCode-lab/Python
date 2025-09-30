#exercicio da aula 07
import time
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

# configurando interface flet
def main(page: ft.Page, ):
    # 1. Configura a janela
    page.title = "MP3 Player"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def tocar():
        # Pergunta a entrada uma única vez dentro do loop
        #play = input("Digite o \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")
        # Esta função será chamada quando o botão for clicado
        if play == 'play':
            pygame.mixer.music.play()
        elif play == 'pause':
            pygame.mixer.music.pause()
        elif play == 'stop':
            pygame.mixer.music.stop()
        else:
            print("Opção inválida. Tente novamente.")
        # Atualiza o botão para mostrar o novo texto
        page.update()

    # Cria o botão, que vai iniciar a música.
    meu_botao = ft.ElevatedButton(text='play',on_click= tocar())

    # Adiciona o botão à página
    page.add(meu_botao)




ft.app(target=main)




