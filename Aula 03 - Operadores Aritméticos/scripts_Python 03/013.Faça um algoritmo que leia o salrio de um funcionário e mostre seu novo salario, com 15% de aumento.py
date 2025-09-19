'''013.Faça um algoritmo que leia o salrio de um funcionário e mostre seu novo salario, com 15% de aumento.'''

valor = float(input('Digite os Valor do Salario ? '))
aumento = float(input('Digite a porcentagem do aumento do Salario ? '))


covertdecimal = aumento /100
print(covertdecimal)
calculoaumento = valor * covertdecimal
print(calculoaumento)
novosalario = calculoaumento + valor
print('O seu antigo salario R${} reais \n O novo salario com {}% de aumento será R${} reais \n Salario Total R${} reais'.format(valor,aumento,calculoaumento,novosalario))