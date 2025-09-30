#Aula 08 - Condições Aninhadas

#estrutura aninhada padrão
'''
if carro.esquerda:
    bloco1
elif carro.direita:
    bloco2
else:
    bloco3
'''

#estrutura aninhada, pode ser usado sem else mais o elif(seNão) não pode sem if.
nome = str(input('Digite seu nome: '))
if nome == 'marcelo':
    print('Que nome bonito!')
elif nome == 'marco':
    print('seu nome bem popular!')
elif nome in 'jessica':
    print('Voce e bonita!')
else:
    print('Seu nome é bem normal!')
print('\033[1;32;40m{}\033[m'.format(nome))

#exercicios

#036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.O programa vai perguntar o valor da casa,
#o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal sabendo que ela não pode executar 30% do salario ou então o emprestimo será negado

#037 - Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera´a base de conversão
#1 para binario
#2 para octal
#3 para hexadecimal

#038 - Escreva um programa que leia dois números inteiros a compare-os. mostrando na tala uma mensagem:
# O primeiro valor é maior O segundo valor é maior Não existe valor maior, os dois são iguais

#039 - Faça um programa qua laia o ano da nascimento da um jovem a informa.da acordo com sua idade:
#- Sa ala ainda vai se alistar ao serviço militar.
#-Sa é a hora de se alistar.
#-Sa já passou do tempo do alistamento.
#Sau programa também davará mostrar o tampo que falta ou que passou do prazo.

#040 - Cria um programa que laia duas notas de um aluno a calcula sua média, mostrando uma mansagem no final. da acordo com a média atingida:
#- Média abaixo da 5.0:REPROVADO
#- Média entra 5.0 a 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior:APROVADO

#041 - A Confederação Nacional de Natação precisa de um programa que laia o ano de nascimento da um atlata a mostra sua catagoria, da acordo com a idade:
#- Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JUNIOR
#- Até 20 anos: SENIOR
#- Acima: MASTER

#042 - Rafaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo sará formado:
#- Equilátero: todos os lados iguais
#-Isóscales: dois lados iguais
#-Escalano: todos os lados diferentes

#043 - Desenvolva uma lógica que laia o paso a a altura da uma pessoa.calcule seu IMC a mostre seu status. de acordo com a tabela abaixo:
#- Abaixo da 18.5: Abaixo do Paso
#- Entre 18.5 a 25: Paso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidada
#Acima de 40: Obesidada mórbida

#044 - Elabora um programa que calcula o valor a ser pago por um produto.considerando o seu prašo normal a condição de pagamento:
#- à vista no cartão: 5% de desconto
#- am até 2x no cartão: praso normal
#-3x ou mais no cartão: 20% de juros

#045 - Cria um programa que faça o computador jogar Jokanpô com você

