#064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 1
c = 0
total = 0
while n != 999:
    c +=1
    n = int(input(f'Digite {c}° numero [999 para parar]: '))
    if n == 999:
        continue
    total += n
print(f'Você digitou {c-1} números e a soma dos numeros: {total}')

#ou
'''
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} números e a soma dos numeros: {soma}')
'''