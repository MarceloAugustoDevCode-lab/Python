#032 - Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.

from datetime import date

ano = int(input('Quantos anos na mesma? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year

if  ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Portanto o ano {} é bissexto.'.format(ano))
else:
    print('Portanto o ano {} não é bissexto'.format(ano))
