#055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
c = 0
maior = 0
menor = 0
for c in range(1,3+1):
    peso = int(input(f'Digite o maior peso {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Total de pessoas com mais de 18 anos são {maior}\nTotal de pessoas com menos de 18 anos são {menor}')