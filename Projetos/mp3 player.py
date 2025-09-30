#exercicio da aula 07
import time
import pygame
import flet as ft
from pyexpat.errors import messages

pygame.init()
# lembrando que as barras tem que ser invertidas "F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3".
# crie uma pasta na pasta principal ou em qualquer pasta do pc e coloque o caminho.
pygame.mixer.music.load(r"F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3")
# "a musica e essa foi que eu comecei a gosta de infomatica."

play = ""
pause = ""
stop = ""



def main(page: ft.Page):
    page.title = "MP3 Player"
    tocando = False

    status = ft.Text("Parado")

    def button_clicked(e):
        nonlocal tocando
        if not tocando:
            pygame.mixer.music.play()
            botao.icon = ft.Icons.PAUSE_CIRCLE_OUTLINED
            status.value = "Tocando!"
            tocando = True
        else:
            pygame.mixer.music.stop()
            botao.icon = ft.Icons.PLAY_CIRCLE_FILL_OUTLINED
            status.value = "Parado!"
            tocando = False

        page.update()

    botao = ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,icon_size=50,on_click=button_clicked,)

    # Corrigindo: usar Column para centralizar
    page.add(ft.Column([botao, status],alignment=ft.MainAxisAlignment.END,horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True))

ft.app(target=main)



