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
