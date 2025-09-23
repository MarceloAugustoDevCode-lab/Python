#021 - Faça um programa em Python que abra e reproduza o audio de um arquivo mp3.
import time
import pygame
pygame.init()
# lembrando que as barras tem que ser invertidas "F:\01 Programas Dev\Estudos\Python\som\01.Power.Rangers.mp3".
# crie uma pasta na pasta principal ou em qualquer pasta do pc e coloque o caminho.
pygame.mixer.music.load("F:/01 Programas Dev/Estudos/Python/som/01.Power.Rangers.mp3")
# "a musica e essa foi que eu comecei a gosta de infomatica."


tocar = pygame.mixer.music.play()


# espera o tempo suficiente (exemplo: 30 segundos)
pygame.time.wait(3000000)

