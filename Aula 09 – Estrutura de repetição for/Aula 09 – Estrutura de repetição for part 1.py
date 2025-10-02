#Aula 09 – Estrutura de repetição for parte 1

#em português:
# laço c no intervalo(1,10):
    #passo
#pega

#em inglês:
#for c in range(1,10):
    #passo
#pega

#codigo de pula laço

# laço c no intervalo(0,3):
    #passo
    #pula
#passo
#pega

#for c in range(0,3):
    #passo
    #pula
#passo
#pega

#codigo pega moeda
# laço c no intervalo(0,3):
    #se moeda
        #pega
    #passo
    #pula
#passo
#pega

#for c in range(0,3):
    #if moeda:
        #pega
    #passo
    #pula
#passo
#pega
'''
#Digite print('oi') 8 vezes.
contador =''
for contador in range(0,9):
    print('\033[1;31;40m{}\033[m'.format(contador), end=' ')
print('\033[1;31;40mFIM\033[m')

#Contando para trâs:
contador2 =''
for contador2 in range(9,0,-1):
    print('\033[1;33;40m{}\033[m'.format(contador2), end=' ')
print('\033[1;31;40mFIM\033[m')

#pulando em 2.
contador =''
for contador in range(0,9,2):
    print('\033[1;32;40m{}\033[m'.format(contador), end=' ')
print('\033[1;31;40mFIM\033[m')

#modo for com input:
n = int(input('Digite um numero: '))
for contador in range(0,n+1):
    print('\033[1;34;40m{}\033[m'.format(contador), end=' ')
print('fim')

#modo 3 input
inicio = int(input('Digite um inicio: '))
fim = int(input('Digite um fim: '))
pulo = int(input('Digite um passo: '))
for contador3 in range(inicio,fim+1,pulo):
    print('\033[1;36;40m{}\033[m'.format(contador3), end=' ')
print('fim')

#modo for com input dentro:
for c in range(0,3):
    t = int(input('Digite um numero: '))
print('fim')

# soma todos numeros do input no for.
soma = 0
for c in range(0,3):
    n = int(input('Digite um numero: '))
    soma += n
print('\033[1;34;40m{}\033[m'.format(soma), end=' ')
'''

#exercicios:

#046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#048 - 