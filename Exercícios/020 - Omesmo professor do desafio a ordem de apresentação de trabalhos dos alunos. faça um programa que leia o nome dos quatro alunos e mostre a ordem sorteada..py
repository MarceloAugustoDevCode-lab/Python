#020
# mesmo professor do desafio a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('digite o nome do primeiro aluno? ')
aluno2 = input('digite o nome do segundo aluno? ')
aluno3 = input('digite o nome do terceiro aluno? ')
aluno4 = input('digite o nome do quarto aluno? ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
listanomes = random.shuffle(lista)
print('o aluno escolhido foi {}'.format(sorteio))
print('A lista da ordem {}'.format(lista))





