#024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.



nome = str(input('Digite o nome da cidade: ')).strip()
print('O nome da Cidade {}'.format(nome[:5].upper() == 'SANTO'))# mostra lista

