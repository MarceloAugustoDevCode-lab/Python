#055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = 0
for c in range(1,3+1):
    pessoas = int(input(f'Digite o maior peso {c}° pessoa: '))
    if pessoas > peso:
        maior = peso
    else:
        menor = peso



print(f'Total de pessoas com mais de 18 anos são {maior}')
print(f'Total de pessoas com menos de 18 anos são {menor}')