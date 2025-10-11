#Aula 11 – Interrompendo repetições while (parte3)
'''

Enquanto verdadeiro:
    se terra:
        passo
    se vazio:
        pula
    se dinheiro:
        paga
    se troféu:
        pula
        interrompe
    pega
'''
# o comando termina utilizando break.
'''
# na forma de python:
while True:
    if terra:
        passo
    if vazio:
        pula
    if dinheiro:
        pula
    if troféu:
        pula
        break
    pega
'''
# a repetição no enquanto utilizando flegs.
#exemplo 1
n=0
while n != 999:
    n = int(input('Digite um numero: '))
#exemplo 2
cont =1
while cont <=10:
    print(cont,' ', end=' ')
    cont += 1
print('FIM')

# utilizando break.
n1 = s = 0
while True:
    n1 = int(input('Digite um numero: '))
    if n1 == 999:
        break
    s += n1
print(f'A soma vale {s}!')

# Exercícios
# 066 - Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

# 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

# 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.