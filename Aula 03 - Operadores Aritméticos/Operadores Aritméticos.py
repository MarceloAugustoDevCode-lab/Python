'''
n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
soma = n1 + n2

print('A soma {} + {} é igual {}.'.format(n1,n2,soma))
'''

# Operadores Arirméticos. ( == igual no Python).

# + no PYTHON Adição
'''
#5+2 ==7

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
soma = n1 + n2

print('A soma {} + {} é igual {}.'.format(n1,n2,soma))
'''

# - no PYTHON Subtração
'''
#5-2 ==3

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
menos = n1 - n2

print('A menos {} - {} é igual {}.'.format(n1,n2,menos))
'''

# * no PYTHON Multiplicação
'''
#5*2 ==10

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
Multiplicação = n1 + n2

print('A vezes {} + {} é igual {}.'.format(n1,n2,Multiplicação))
'''

# / no PYTHON Divisão
'''
#5/2 ==2.5

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
Divisão = n1 / n2

print('A Divisão {} - {} é igual {}.'.format(n1,n2,Divisão))
'''

# ** no PYTHON Potência ou raiz quadrada
'''
#5**2 ==25 ou pow(5,2) pde ser feita assim tambem 81**(1/2):
# Raiz Cubica 127**(1/3)

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
Potência = n1 ** n2

print('A Potência {} - {} é igual {}.'.format(n1,n2,Potência))
'''

# // no PYTHON Divisão Inteira
'''
#5//2 ==2

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
DivisãoInteira = n1 // n2

print('A Divisão Inteira {} - {} é igual {}.'.format(n1,n2,DivisãoInteira))
'''

# % no PYTHON Resto da Divisão
'''
#5%2 ==1

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
RestoDivisão = n1 % n2

print('A Resto da Divisão {} - {} é igual {}.'.format(n1,n2,RestoDivisão))
'''

# Ordem de Precedência:
'''
1 ()
2 **
3 *,/,//,%
4 +,-
'''

# Exercicios 01 explicação:
'''
#5+3*2==11

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
n3 = int(input('Digite o Terceiro Numero ? '))
conta = n1 + n2 * n3

print('O resultado da expressão matemática de {} + {} * {} é igual {}.'.format(n1,n2,n3,conta))
'''

# Exercicios 02 explicação:
'''
#3*5+4**2==31

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
n3 = int(input('Digite o Terceiro Numero ? '))
n4 = int(input('Digite o Quarto Numero ? '))
conta = n1 * n2 + n3 ** n4

print('O resultado da expressão matemática de {} + {} * {} ** {} é igual {}.'.format(n1,n2,n3,n4,conta))
'''

# Exercicios 03 explicação:
'''
#3*(5+4)**2==31

n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
n3 = int(input('Digite o Terceiro Numero ? '))
n4 = int(input('Digite o Quarto Numero ? '))
conta = n1 * (n2 + n3) ** n4

print('O resultado da expressão matemática de {} + {} * {} ** {} é igual {}.'.format(n1,n2,n3,n4,conta))
'''

'''
# concatenando:
print('oi' + 'ola')
# oi qualquer letra 5 vezes na tela
print('oi'*5)
'''

'''
#O código fornecido demonstra a formatação de texto e alinhamento na linguagem de programação Python.
nome = input('Qual é seu nome ? ')
print('Prazer em te Conhecer {:20}!'.format(nome))
print('Prazer em te Conhecer {:>20}!'.format(nome))
print('Prazer em te Conhecer {:<20}!'.format(nome))
print('Prazer em te Conhecer {:^20}!'.format(nome))
print('Prazer em te Conhecer {:=^20}!'.format(nome))
'''

'''
# Exercicios 04:
n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
print('O resultado da expressão matemática é igual {}.'.format(n1 + n2))
'''

'''
# Exercicios 05:
n1 = int(input('Digite o Numero ? '))
n2 = int(input('Digite o Segundo Numero ? '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('O resultado da expressão matemática, soma {} e multiplicação {} e a divisão {}.'.format(s,m,d))
print('O resultado da expressão matemática, Divisão inteira {} e potência {}'.format(di,e))
print('O resultado da expressão matemática, divisão usando da forma que esta do lado{:.3f}.'.format(d))
print('O resultado da expressão matemática, soma {}, \n e multiplicação {}, \n e a divisão {}.'.format(s,m,d))
print('O resultado da expressão matemática, soma {} e multiplicação {} e a divisão {:.3f}.'.format(s,m,d), end=' ')
print('O resultado da expressão matemática, divisão {:.3f}.'.format(s,m,d), end='>>>')
'''


#005.Faça um programa que leia um numero inteiro o seu sucessor e seu antecessor.
'''005.Faça um programa que leia um numero inteiro o seu sucessor e seu antecessor.'''
numero = int(input('Digite o Numero Inteiro ? '))
nsucessor = numero + 1
nantecessor = numero - 1

print('O Numero Inteiro é {}, o Numero Sucessor é {} e o Antecessor {}.'.format(numero,nsucessor,nantecessor))


#006.Crie um algoritmo que leia um numero e mostre o seu dobro triplo e raiz quadrada.
'''006.Crie um algoritmo que leia um numero e mostre o seu dobro triplo e raiz quadrada.'''
numero = int(input('Digite o Numero Inteiro ? '))
dobro = numero * 2
triplo = numero * 3
potencia = numero ** 2

print('O Numero é {}, Dobro é {}, o Triplo e {}, Raiz Quadrada é {} .'.format(numero,dobro,triplo,potencia))


#007.Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
'''007.Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.'''
n1 = int(input('Digite o Nota 1 ? '))
n2 = int(input('Digite o Nota 2 ? '))
soma = n1 + n2 
media = soma / 2

print('A sua Media é ',media)


#008.Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''008.Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
metros = int(input('Digite os Metros ? '))
centimetros = metros * 100
milimetros = centimetros * 10

print('{} Metros, convertido em centímetros é {} e Milímetros é {}'.format(metros,centimetros,milimetros))

#009.Faça um progrma que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
'''009.Faça um progrma que leia um numero inteiro qualquer e mostre na tela a sua tabuada.'''
numero = int(input('Digite o numero ? '))

#tabela 01
t0 = numero * 0
t1 = numero * 1
t2 = numero * 2
t3 = numero * 3
t4 = numero * 4
t5 = numero * 5
t6 = numero * 6
t7 = numero * 7
t8 = numero * 8
t9 = numero * 9
t10 = numero * 10

print(' Tabuada de {} \n {} x 0 = {} \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(numero,numero,t0,numero,t1,numero,t2,numero,t3,numero,t4,numero,t5,numero,t6,numero,t7,numero,t8,numero,t9,numero,t10))

#010.Crie um um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$1,00= R$3,27)
'''010.Crie um um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$1,00= R$3,27)'''
dinheiro = int(input('Quanto você tem em Dinheiro ? '))
conversao = dinheiro / 5,35

print('Na minha Carteira tem ',dinheiro,' posso comprar',conversao,' Dólares')

#011.Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2quadrado.
'''011.Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2quadrado.'''

largura = int(input('Digite a largura ? '))
altura = int(input('Digite a altura ? '))
extra = int(input('Se houver portas ou janelas, calcule e some e coloque Aqui ? '))

total = (largura * altura) - extra
print(total)
area = total/2
demaos = area * 2
print('Sabendo que 1 litro de tinta pinta 2m², Calculo da quantidade de tinta necessária é {} litros de tinta e se for 2 demãos é {} litros de tinta'.format(area,demaos))

#012.Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.
'''012.Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.'''

valor = float(input('Digite os Valor do Produto ? '))
desconto = float(input('Digite os Desconto do Produto ? '))

porcetagem = 100 - desconto
covertdecimal = porcetagem /100
novopr = valor * covertdecimal

print('O novo preço com {}% de desconto será R$ {} reais'.format(desconto,novopr))
#013.Faça um algoritmo que leia o salrio de um funcionário e mostre seu novo salario, com 15% de aumento.
'''013.Faça um algoritmo que leia o salrio de um funcionário e mostre seu novo salario, com 15% de aumento.'''

valor = float(input('Digite os Valor do Salario ? '))
aumento = float(input('Digite a porcentagem do aumento do Salario ? '))


covertdecimal = aumento /100
print(covertdecimal)
calculoaumento = valor * covertdecimal
print(calculoaumento)
novosalario = calculoaumento + valor
print('O seu antigo salario R${} reais \n O novo salario com {}% de aumento será R${} reais \n Salario Total R${} reais'.format(valor,aumento,calculoaumento,novosalario))