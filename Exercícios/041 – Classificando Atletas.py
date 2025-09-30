#041 - A Confederação Nacional de Natação precisa de um programa que laia o ano de nascimento da um atlata a mostra sua catagoria, da acordo com a idade:
#- Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JUNIOR
#- Até 25 anos: SENIOR
#- Acima: MASTER

idade = int(input('Digite sua idade: '))
print('O atleta tem {} anos.'.format(idade))

if idade == 1 or idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade == 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

#OU
'''
from datetime import date

atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
'''