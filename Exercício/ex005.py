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
