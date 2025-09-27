#Ele vai colocar na memoria do computador so que ele vai botar mini espaço.
#exemplo:
frase = 'Curso em Video Python'
#        0123456789101112131415161718192021 E o numero caracteres incluindo o espaço do texto. indice.

'''
#fatiamento:string
'''
'''
print(frase[9])#O 9 e a letra V da frase curso em video.

print(frase[9:13])#Ele vai escolhe do 9 ate 13 mais excluir o 13 pois no python ele vai conta ate 12.

print(frase[9:21])#Ele vai escolhe do 9 ate 21 mais excluir o 13 pois no python ele vai conta ate 12.

print(frase[9:21:2])#Dessa forma ele vai começar com V so que ele vai pulando em 2 em 2 VxdxoxPxtxo ficara VdoPto.

print(frase[:5])#Desse jeito ele vai do inicio até 5 que o fim.

print(frase[15:])#Desse jeito ele vai do 15 ate o 21 nesse caso.

print(frase[9::3])#Dessa forma ele vai começar 9 e vai ate o final so que ele vai pular em 3 em 3 VePh.
'''
# -----------------------------------------------------------------------------
'''
'''
#Análise
#len em portugues e comprimento.
'''
print('A frase tem' ,len(frase), 'letras incluindo o espaço.')


'''
#count ele vai contar quantas letras tem ha letra escolida.
'''
print('Ele tem' ,frase.count('o'), 'três eletras.')
print(frase.count('o',0,13)) # Ele vai do 0 ao 12 pois no python o 13 e excluido ele e como de 0 a 12 so tem 1 'o'


'''
#find eu encontro uma palavra ou qualquer letra no texto.
'''
print(frase.find('deo'))
'''


'''
# Operador IN em Português é EM.
'''
print('Curso' in frase) #Se estiver escrito ele vai dizer true/sim ou false/não.

'''
# Transformação 
'''
'''
#Replace e troca ou reposicionar.
print(frase.replace('Python','android'))# onde na frase estiver python vai ser substituido por android

print(frase.upper()) #ficara em Maisculo.

print(frase.lower()) #Ficara em Minusculo.

print(frase.capitalize()) #Ele vai coloca em Maisculo a primeira letra.

print(frase.title()) #Ele vai colocar em maisculo em cada começo de palavra. 

print(frase.strip()) #Ele remove todos os espaços inutes no começo e no fim

print(frase.rstrip()) #Ele vai remover so ultimo espaço da direita.

print(frase.lstrip()) #Ele vai remover so ultimo espaço da esquerda.

print(frase.split()) #Ele faz que cada palavra receber indexação nova ele vai dividir em uma lista.

'''
'''
#Junção
'''
print(' '.join(frase))

#Exercicios

#022 - Crie um programa que leia o nome completo de uma pessoa e mostre(
# o nome com todas as letras maiúsculas,o nome com todas as letras minúsculas.
#Quantas letras ao todoq (sem considerar espaços e quantas eletras tem o primeiro nome.

#023 - Faça um programa que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados.
#ex digite um numero: 1834 unidade:4 , dezena:3 , centena:8 , milhar:1

#024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.

#025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

#026 - Faça um programa que leia uma frase pelo teclado e mostre:
#quantos vezes aparece a letra "A", em que posição ela aparece a primeira vez.
#em que posição ela aparece a ultima vez.

#027 - Crie um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#ex ana maria de souza
#primeiro = ana
#ultimo = souza
