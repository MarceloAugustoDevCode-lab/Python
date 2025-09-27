#025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Digite o nome: ')).strip()
nome = nome.upper()
tem =  'SILVA' in nome
print('O nome {} ela tem silva no nome {}'.format(nome,tem))# mostra lista

