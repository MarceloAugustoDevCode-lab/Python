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
    print('\033[1;33;40m{}\033[m'.format(contador), end=' ')
print('fim')