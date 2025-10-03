
import flet as ft


def main(page: ft.Page):
    # adicionar controles na pagina
    # nome da pagina
    page.title = "Mp3 Player"
    page.padding = 0
    page.window.width = 450
    page.window.height = 550




    page.update()


ft.app(port=8550,target=main)