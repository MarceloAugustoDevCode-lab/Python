#053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]
#ou com for
'''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
'''
print(junto,' / ', inverso,end=' ''= ')
if inverso == junto:
    print('E palíndromo')
else:
    print('Não é palíndromo')
