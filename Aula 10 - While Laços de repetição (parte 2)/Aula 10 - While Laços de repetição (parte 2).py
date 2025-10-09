#Aula 10 - While Laços de repetição (parte 2)

#enquanto = while
#Estrutura de repetição teste lógico.

'''
enquanto não variavel:
    passo
pega


while not variavel:
    passo
pega
'''

'''
enquanto não variavel:
    se variavel1
        passo
    se variavel2
        palu
    se variavel3
        pega
pega

while not variavel:
    if variavel1:
        passo
    if variavel2:
        pula
    if variavel3:
        pega
pega
'''
'''
#exemplo 1 com while
c =1
while c < 10:
    print(c)
    c += 1
print('fim')

#exemplo 2 com while condição de parada.
n=1
while n != 0:
    n= int(input('Digite um numero: '))
print('fim')
'''
'''
#exemplo 3 com while condição de parada com string.
r ='S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print('fim')
'''
#exemplo 4 com while condição de parada com n par ou impar.LEMBRANDO QUANDO EU DIGITAR 0 ELE PARA. EU ESQUECI KKK.
nt = 1
par = 0
impar = 0
while nt != 0:
    nt = int(input('Digite um numero: '))
    if nt % 2 == 0:
        par +=1
    else:
        impar +=1
print(f'Você digitou {par} numeros pares e {impar} numeros impares')

# parte break e continue fica para proxima aula.

#exercicios:


#057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#058 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#059 - Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

#060 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#061 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#062 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0     –   1   –   1   – 2 – 3 – 5 – 8
#termo - termo2

#064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#065 - Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
















