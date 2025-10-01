#044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

valor = int(input('Digite sua valor do Produto: '))
escolha = str(input('Digite sua escolha: \033[1;31;40mA\033[m a vista ou \033[1;32;40mB\033[m cartão a vista ou \033[1;35;40mC\033[m cartão ate 2x vezes sem juros ou \033[1;34;40mD\033[m em 3x + 20% de juros ?')).upper()
vista ='A'
cartao ='B'
parcela2x='C'
parcela3x='D'
if escolha == 'A' or escolha == 'B' or escolha == 'C' or escolha == 'D':
    if escolha == 'A':
        avista = valor  * 10 / 100 # porcentagem 30% / 100%
        avista = valor - avista
        print('\033[1;32;40mà vista dinheiro/cheque: 10% de desconto,\033[m\033[1;31;40mTOTAL R${} reais\033[m'.format(avista))
    elif escolha == 'B':
        cartao = valor * 5 / 100
        cartao = valor - cartao
        print('\033[1;32;40mà vista no cartão: 5% de desconto,\033[m\033[1;32;40mTOTAL R${} reais\033[m'.format(cartao))
    elif escolha == 'C':
        parcela2x = valor / 2
        print('\033[1;32;40mParcela em até 2x no cartão: preço formal,\033[m\033[1;35;40mTOTAL R${} reais cada mêS\033[m'.format(parcela2x))
    elif escolha == 'D':
        parcela3x = valor * 20 / 100 # porcentagem 30% / 100%
        parcela3x = valor + parcela3x
        parcela3x = (parcela3x /3)
        print('\033[1;32;40mParcela em até 3x ou mais no cartão: 20% de juros,\033[m\033[1;34;40mTOTAL R${} reais\033[m'.format(parcela3x))
else:
    print('tente novamente')
