# Exercício Python 15:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Pergunte ao usuário a quantidade de dias pelos quais o carro foi alugado ? '))
km = float(input('Pergunte ao usuário a quantidade de quilômetros percorridos pelo carro ? '))

pago = (dias * 60) + (km * 0.15)

print('Portanto, o preço a pagar seria R$',pago)