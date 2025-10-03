#054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

ano_atual = datetime.date.today().year

maior = 0
menor = 0
for c in range(1,7+1):
    ano_nascimento = int(input(f'Digite o ano de {c}° nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade > 18:
        maior+=1
    else:
        menor+=1



print(f'Total de pessoas com mais de 18 anos são {maior}')
print(f'Total de pessoas com menos de 18 anos são {menor}')



#print(nome, ano_nascimento,end=' ')




