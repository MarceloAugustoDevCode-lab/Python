# Aula 06 Aula 06 - Condições em Python
#estrutura de sequencia: condicionais.

'''
#vou explicar de modo rapido. primeiro vou criar uma variavel com nome de nome:
nome = input('Digite seu nome: ')
# depois criar outra variavel com nome de escolha para dar a função do if(se) e else(senão)
escolha = input('escolha se maiúsculo ou minúsculo se nao aperte enter: ')

#se eu quero que nome fique Maiúsculo o vou escrever maiúsculo , if no python e (se).
if escolha == 'maiúsculo':# se escolha for (==) igual string 'maiúsculo' ficara maiúsculo
    print(nome.upper())#função que altera para maiúsculo

#senão eu quero que nome fique Minúsculo o vou escrever qualquer outra se Minúsculo, else no python e (senão).
else:#senão a escolha sera minúsculo
    print(nome.lower())#função que altera para minúsculo
'''
'''
tempo = int(input('Quantos anos tem seu carro ? '))

if tempo <= 3 :
    print('carro novo')
else:
    print('carro carro velho')
print('--FIM--')
'''

#ou

'''
tempo = int(input('Quantos anos tem seu carro ? '))
print('carro novo'if tempo <=3 else 'carro velho'))
print('--FIM--')
'''
'''
# Condicional Simples:-------------------------
nome = str(input('Digite seu nome: '))
if nome == 'Marcelo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))
#----------------------------------------------
'''
'''
# Condicional Composta:-------------------------
nome = str(input('Digite seu nome: '))
if nome == 'Marcelo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
#-----------------------------------------------
'''
'''
# Media do aluno:
n1 = float(input('Digite sua primeira nota: ')) 
n2 = float(input('Digite sua segundo nota: '))
m = (n1 + n2) / 2
if m >= 6 :
    print('Sua media foi boa! Parabens!')
else:
    print('Sua media foi ruim! Estude mais!')
'''
# ou
'''
# Media do aluno:
n1 = float(input('Digite sua primeira nota: ')) 
n2 = float(input('Digite sua segundo nota: '))
m = (n1 + n2) / 2
print('Sua media foi boa! Parabens'if m >=6 else 'Sua media foi ruim! Estude mais!')
'''
#Exercicios.
#028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#029 - Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,oo reias por cada Km acima do limite.

#030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Impar.

#031 - Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem,cobrado R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

#032 - Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.

#033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$1.250.00, calcule um aumento de 10%
#para os inferiores ou iguais e aumento e de 15%.

#035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.