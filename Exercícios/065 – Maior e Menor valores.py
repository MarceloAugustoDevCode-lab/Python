#065 - Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from dearpygui.dearpygui import reset_pos
from django.template.context_processors import media

resposta = 'Ss'
n = 0
c = 0
total = 0
maior = 0
menor = 0
media = 0
while resposta in 'Ss':
    c +=1
    n = int(input(f'Digite {c}° numero: '))

    total += n
    media = total / 2
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você digitou {c-1} números e a soma dos numeros: {total}\nA media do total dos numeros {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')



