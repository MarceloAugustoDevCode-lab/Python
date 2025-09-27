#026 - Faça um programa que leia uma frase pelo teclado e mostre:
#quantos vezes aparece a letra "A", em que posição ela aparece a primeira vez.
#em que posição ela aparece a ultima vez.

# frase de ex: marcelo bonitão kkk

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()


print('A letra A aparece {} vezes na frase'.format(frase.count('A',0,13))) # Ele vai do 0 ao 12 pois no python o 13 e excluido ele e como de 0 a 12 so tem 1 'o'
print('A letra A aparece na posição',frase.find('A')+1)
print('A última letra A apareceu na posição',frase.rfind('A')+1)