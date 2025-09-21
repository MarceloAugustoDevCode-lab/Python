#019
#Um Professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = input('digite o nome do primeiro aluno? ')
aluno2 = input('digite o nome do segundo aluno? ')
aluno3 = input('digite o nome do terceiro aluno? ')
aluno4 = input('digite o nome do quarto aluno? ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('o aluno escolhido foi {}'.format(sorteio))