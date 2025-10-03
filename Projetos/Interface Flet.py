# interface Flet
import flet as ft


def main(page: ft.Page):
    # adicionar controles na pagina
    # nome da pagina
    page.title = "Mp3 Player"
    page.padding = 0
    page.window.width = 450
    page.window.height = 550
    page.update()

    #texto
    page.add(ft.Text('Ola'))

    # container botão ----------------------------------
    c1 = ft.Container(
        content = ft.ElevatedButton('Botão'),
        #bgcolor= "#55555", COR
        padding= 10,
    )

    # adicionando o container
    page.add(c1)
    #---------------------------------------------------

    # container botão ----------------------------------
    c2 = ft.Container(
        content = ft.ElevatedButton('>'),
        #bgcolor= "#55555", COR
        padding= 10,
    )

    # adicionando o container
    page.add(c2)
    #---------------------------------------------------

    # container botão ----------------------------------
    c3 = ft.Container(
        content=ft.ElevatedButton('<'),
        # bgcolor= "#55555", COR
        padding=10,
    )

    # adicionando o container
    page.add(c3)
    # ---------------------------------------------------

ft.app(port=8550,target=main)