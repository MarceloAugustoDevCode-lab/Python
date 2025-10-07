#054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

ano_atual = datetime.date.today().year
c =0
maior = 0
menor = 0
for c in range(1,2+1):
    ano_nascimento = int(input(f'Digite o ano de {c}° nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade > 18:
        maior+=1

    if idade < 18:
        menor+=1
maiorv = maior
menorv = menor
print(f'Total de pessoas com mais de 18 anos são {maiorv}\nTotal de pessoas com menos de 18 anos são {menorv}')




#print(nome, ano_nascimento,end=' ')




