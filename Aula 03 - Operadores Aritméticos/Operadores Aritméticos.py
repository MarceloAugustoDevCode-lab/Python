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
# Desafios atenção ele estao na pasta Exercícios pronto faça primeiro depois confere.

#005.Faça um programa que leia um numero inteiro o seu sucessor e seu antecessor.

#006.Crie um algoritmo que leia um numero e mostre o seu dobro triplo e raiz quadrada.

#007.Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

#008.Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#009.Faça um progrma que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

#010.Crie um um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$1,00= R$3,27)

#011.Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2quadrado.

#012.Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.

#013.Faça um algoritmo que leia o salrio de um funcionário e mostre seu novo salario, com 15% de aumento.
