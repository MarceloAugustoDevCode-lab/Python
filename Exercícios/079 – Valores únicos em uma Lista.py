
pergunta = 'Ss'
c = 0
valores = []
while True:
    c+=1
    n = (int(input(f'Digite um valor para a posição {c}:  ')))
    valores.append(n)
    if c == 2 and n == n:
        print('valor duplicado, não vou adicionar...')
        valores.remove(n)
        pass
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta in 'Nn':
        break
    sorted(valores)
print(f'Você digitou os valores {valores}')

