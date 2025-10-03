# interface Flet
import flet as ft
from flet.core.column import Column
from flet.core.stack import Stack


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
    cb1 = ft.Container(
        content = ft.ElevatedButton('Botão'),
        #bgcolor= "#55555", COR
        padding= 10,
    )

    # adicionando o container
    page.add(cb1)
    #---------------------------------------------------

    # container botão ----------------------------------
    cb2 = ft.Container(
        content = ft.ElevatedButton('>'),
        #bgcolor= "#55555", COR
        padding= 10,
    )

    # adicionando o container
    page.add(cb2)
    #---------------------------------------------------

    # container botão ----------------------------------
    cb3 = ft.Container(
        content=ft.ElevatedButton('<'),
        # bgcolor= "#55555", COR
        padding=10,
    )

    # adicionando o container
    page.add(cb3)
    # ---------------------------------------------------



    # ROW
    # ----------------------------------------------------
    # container botão
    r1 = ft.Container(
        content = ft.ElevatedButton('Botão'),
        #bgcolor= "#55555", COR
        padding= 10,
    )
    # container botão
    r2 = ft.Container(
        content = ft.ElevatedButton('>'),
        #bgcolor= "#55555", COR
        padding= 10,
    )
    # container botão
    r3 = ft.Container(
        content=ft.ElevatedButton('<'),
        # bgcolor= "#55555", COR
        padding=10,
    )
    # Lista de Controles de cima
    item = [r1,r2,r3]
    #ROW

    #Criando ROW
    row = ft.Row(spacing=5,controls= item)

    # adicionando o container
    page.add(row)
    #----------------------------------------------------

    #---------------------------------------------------
    # Criando coluna
    # container botão
    c1 = ft.Container(
        content = ft.ElevatedButton('Botão'),
        #bgcolor= "#55555", COR
        padding= 10,
    )
    # container botão
    c2 = ft.Container(
        content = ft.ElevatedButton('>'),
        #bgcolor= "#55555", COR
        padding= 10,
    )
    # container botão
    c3 = ft.Container(
        content=ft.ElevatedButton('<'),
        # bgcolor= "#55555", COR
        padding=10,
    )
    # Lista de Controles de cima
    item2 = [c1,c2,c3]
    Coluna =ft.Column(spacing=5,controls=item2)
    page.add(Coluna)
    #---------------------------------------------------


    #stack
    #----------------------------------------------------
    # Criando stack
    st = ft.Stack(
[
        ft.ElevatedButton('Botão1'),
        ft.Image(
            src=f"Flamengo.png",
            width = 150,
            height = 150
    )
        ],width=300,height=300,)
    page.add(st)
    # ----------------------------------------------------

    #STACK POR BAIXO DOS BOTÕES
    # stack
    # ----------------------------------------------------
    # Criando stack
    st1 = ft.Stack(
        [
            ft.ElevatedButton('Botão12'),
            ft.Image(
                src=f"Flamengo.png",
                width=150,
                height=150
            ),
            row,
        ], width=500, height=300, )
    page.add(st1)
    # ----------------------------------------------------


ft.app(port=8550,target=main)