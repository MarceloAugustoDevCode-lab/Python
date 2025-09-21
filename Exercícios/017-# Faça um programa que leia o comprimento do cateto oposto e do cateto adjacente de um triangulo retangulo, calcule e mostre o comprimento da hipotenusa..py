#017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

'''
import math
# entrada de dados.
coposto = float(input('Digite o comprimento do cateto oposto? '))
cadjacente = float(input('Digite o comprimento do cateto adjacente? '))
#Calcular a hipotenusa:
hipotenusa = math.hypot(coposto, cadjacente)
print('O mostre o comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
'''

#ou sem o import math.
# entrada de dados.
oposto = float(input('Digite o comprimento do cateto oposto? '))
adjacente = float(input('Digite o comprimento do cateto adjacente? '))
#Calcular a hipotenusa:
hipotenusa2 = (coposto ** 2 + cadjacente ** 2) ** (1/2)
print('O mostre o comprimento da hipotenusa é {:.2f}'.format(hipotenusa2))



