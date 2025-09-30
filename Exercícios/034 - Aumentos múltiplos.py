#034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$1.250.00, calcule um aumento de 10%
#para os inferiores ou iguais e aumento e de 15%.



valor = float(input('Digite os Valor do Salario ? '))

if valor <= 1250:
    novo = valor + (valor * 15 / 100)
else:
    novo = valor + (valor * 10 / 100)
print('O seu antigo salario R${} reais \n O novo salario aumento será R${} reais'.format(valor,novo))

#ou


'''
if valor <= 1250:
    aumento = 15
    covertdecimal = aumento / 100
    calculoaumento = valor * covertdecimal
    novosalario = calculoaumento + valor

    print('O seu antigo salario R${} reais \n O novo salario com {}% de aumento será R${} reais \n Salario Total R${} reais'.format(valor,aumento,calculoaumento,novosalario))
else:
    aumento = 10
    covertdecimal = aumento / 100
    calculoaumento = valor * covertdecimal
    novosalario = calculoaumento + valor
    print('O seu antigo salario R${} reais \n O novo salario com {}% de aumento será R${} reais \n Salario Total R${} reais'.format(valor,aumento,calculoaumento,novosalario))
'''
