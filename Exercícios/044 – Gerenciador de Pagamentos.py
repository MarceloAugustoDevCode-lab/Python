#044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

valor = int(input('Digite sua valor: '))
escolha = int(input('Digite sua escolha: '1' a vista ou '2' cartão a vista ou '3' cartão ate 2x vezes sem juros ou em 3x + 20% de juros '))
if escolha == 1:
    avista = valor  * 10 / 100 # porcentagem 30% / 100%
    avista = valor - avista
    print('à vista dinheiro/cheque: 10% de desconto,TOTAL R${} reais'.format(avista))
if escolha == 2:
    cartao = valor * 5 / 100
    cartao = valor - cartao
    print('à vista no cartão: 5% de desconto,TOTAL R${} reais'.format(cartao))

parcela2x = valor / 2
print('Parcela em até 2x no cartão: preço formal,TOTAL R${} reais'.format(parcela2x))


parcela3x = valor * 20 / 100 # porcentagem 30% / 100%
parcela3x = valor + parcela3x
parcela3x = (parcela3x /3)
print('Parcela em até 3x ou mais no cartão: 20% de juros,TOTAL R${} reais'.format(parcela3x))