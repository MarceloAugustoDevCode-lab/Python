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







