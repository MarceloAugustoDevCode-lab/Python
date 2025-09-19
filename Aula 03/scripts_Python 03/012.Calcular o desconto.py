'''012.Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.'''

valor = float(input('Digite os Valor do Produto ? '))
desconto = float(input('Digite os Desconto do Produto ? '))

porcetagem = 100 - desconto
covertdecimal = porcetagem /100
novopr = valor * covertdecimal

print('O novo preço com {}% de desconto será R$ {} reais'.format(desconto,novopr))


