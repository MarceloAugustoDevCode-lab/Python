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
while play != 'stop':
    play = input("Digite o \033[1;31;40m'play'\033[m para tocar \033[1;31;40m'pause'\033[m para parar e \033[1;31;40m'stop'\033[m para sair: ")

    if play == 'play':
        pygame.mixer.music.play()
    elif play == 'pause':
        pygame.mixer.music.pause()
    elif play == 'stop':
        pygame.mixer.music.stop()
    else:
        print("Opção inválida. Tente novamente.")


def botao_pause(e):
    # A função muda o valor da mensagem para um novo texto
    mensagem.value = "Tocando!" and pygame.mixer.music.pause()

    # Avisa ao Flet para atualizar a tela e mostrar a mudança
    page.update()

    # 3. Cria o botão e o conecta à função 'botao_clicado'


botao = ft.ElevatedButton(text="Clique aqui", on_click=botao_pause)

# 4. Adiciona o texto e o botão à página
page.add(mensagem, botao)


def botao_stop(e):
    # A função muda o valor da mensagem para um novo texto
    mensagem.value = "Tocando!" and pygame.mixer.music.stop()

    # Avisa ao Flet para atualizar a tela e mostrar a mudança
    page.update()


# 3. Cria o botão e o conecta à função 'botao_clicado'
botao = ft.ElevatedButton(text="Clique aqui", on_click=botao_stop)

# 4. Adiciona o texto e o botão à página
page.add(mensagem, botao)

page.add(ft.Stack([ft.Column([ft.ElevatedButton(text="Botão"),ft.Text("Status: OK", size=16),],top=50,left=50,)],expand=True))