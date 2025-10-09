#065 - Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from django.template.context_processors import media

n = 1
c = 0
total = 0
maior = 0
menor = 0
media = 0
while n != 999:
    c +=1
    n = int(input(f'Digite {c}° numero [999 para parar]: '))
    if n == 999:
        continue
    total += n
    media = total / 2
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou {c-1} números e a soma dos numeros: {total}\nA media do total dos numeros {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')



