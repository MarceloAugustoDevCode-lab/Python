# 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
c = 0
produto = 0
produtocaro =0
nomebarato =''
produtobarato =0
continuar = 'S'
print(30*'-')
print('MERCADO')
print(30*'-')
while True:
    c +=1
    nome = str(input('Digite seu nome do Produto: ')).strip().upper()
    produto = float(input('Digite o preço R$: '))
    #total dos produtos
    total += produto
    #maior que 1000
    if produto > 1000:
       produtocaro += 1
   # menor produto
    if c == 1:
        nomebarato = nome
        produtobarato = produto
    else:
        if produto < produtobarato:
            produtobarato = produto
    #continua
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar =='N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {produtocaro} produtos custando R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${produtobarato:.2f}')
