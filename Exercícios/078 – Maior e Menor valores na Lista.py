
c= 0
contador2 = 0
valores = []

for c in range(1, 6):
    n = int(input(f'Digite um valor para a posição {c}: '))
    valores.append(n)
maior_valor = max(valores)
menor_valor = min(valores)

for pos,maior in enumerate(valores):
    if maior== max(valores):
        c += 1
        if c == 2:
            maior = pos
            break
for pos,menor in enumerate(valores):
    if menor== min(valores):
        contador2 += 1
        if contador2 == 2:
            menor = pos
            break
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posiçôes {valores.index(maior_valor)}')
print(f'O menor valor digitado foi {min(valores)} nas posiçôes {valores.index(menor_valor)}')