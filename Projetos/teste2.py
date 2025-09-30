

def main(page: ft.Page):
    # Configura a janela
    page.title = "MP3 Player"


    tocando = False  # estado da música

    # texto que mostra status
    status = ft.Text("Parado")

    # função chamada ao clicar no botão
    def button_clicked(e):
        nonlocal tocando
        if not tocando:
            pygame.mixer.music.play()
            botao.icon = ft.Icons.PAUSE_CIRCLE_OUTLINED
            status.value = "Tocando!"
            tocando = True
        elif tocando:
            pygame.mixer.music.stop()
            botao.icon = ft.Icons.STOP_CIRCLE_OUTLINED
            status.value = "Parado!"
            tocando = False
        else:
            pygame.mixer.music.pause()
            botao.icon = ft.Icons.PLAY_CIRCLE_FILL_OUTLINED
            status.value = "Pausado!"
            tocando = False

        page.update()

    # botão
    botao = ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,icon_size=30,on_click=button_clicked)

    # Usando Column para alinhar no centro
    page.add((([botao,status]),alignment = ft.alignment.top_center,horizontal_alignment = ft.alignment.top_center))
    page.update()

ft.app(target=main)