


import random

numeros = (random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))
maior =sorted(numeros)[-1]
menor = sorted(numeros)[-4]

print(f'Os valores sorteados foram: {numeros}')
print(f'o maior numero é {maior}')
print(f'O menor numero é {menor}')