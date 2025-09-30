#036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.O programa vai perguntar o valor da casa,
#o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal sabendo que ela não pode executar 30% do salario ou então o emprestimo será negado

valor =int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do seu salário: '))
anos = int(input('Quantos anos de financiamento? '))

minimo = salario * 30 / 100 # porcentagem 30% / 100%
prestacao = valor / (anos*12)

if minimo <= prestacao:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f} Reais o \033[1;31;40mEmpréstimo foi Negado.\033[m'.format(valor, anos, prestacao))
else:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f} Reais o \033[1;32;40mEmpréstimo foi Aprovado.\033[m'.format(valor, anos, prestacao))


