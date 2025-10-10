# 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

c = 0
valor = 1
while True:
    if c >= 10:
        c =0
        valor = int(input('Digite um numero: [Digite numero negativo para sair] '))
    elif c == 0:
        valor = int(input('Digite um numero: [Digite numero negativo para sair] '))
    if valor < 0:
        break
    c +=1
    total = c * valor
    print(f'{c} X {valor} = {total}')


