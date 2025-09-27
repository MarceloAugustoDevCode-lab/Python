# Desafio 005

# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite o Numero Inteiro ? '))
nsucessor = numero + 1
nantecessor = numero - 1

print('O Numero Inteiro é {}, o Numero Antecessor é {} e o Sucessor {}.'.format(numero,nantecessor,nsucessor))
