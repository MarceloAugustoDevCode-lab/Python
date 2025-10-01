#044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

valor = int(input('Digite sua valor: '))
escolha = str(input('Digite sua escolha: A a vista ou B cartão a vista ou C cartão ate 2x vezes sem juros ou D em 3x + 20% de juros ?')).upper()
vista ='A'
cartao ='B'
parcela2x='C'
parcela3x='D'
if escolha == 'A' or escolha == 'B' or escolha == 'C' or escolha == 'D':
    if escolha == 'A':
        avista = valor  * 10 / 100 # porcentagem 30% / 100%
        avista = valor - avista
        print('à vista dinheiro/cheque: 10% de desconto,TOTAL R${} reais'.format(avista))
    elif escolha == 'B':
        cartao = valor * 5 / 100
        cartao = valor - cartao
        print('à vista no cartão: 5% de desconto,TOTAL R${} reais'.format(cartao))
    elif escolha == 'C':
        parcela2x = valor / 2
        print('Parcela em até 2x no cartão: preço formal,TOTAL R${} reais'.format(parcela2x))
    elif escolha == 'D':
        parcela3x = valor * 20 / 100 # porcentagem 30% / 100%
        parcela3x = valor + parcela3x
        parcela3x = (parcela3x /3)
        print('Parcela em até 3x ou mais no cartão: 20% de juros,TOTAL R${} reais'.format(parcela3x))
else:
    print('tente novamente')
