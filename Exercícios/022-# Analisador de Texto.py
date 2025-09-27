#022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas,
# o nome com todas as letras minúsculas.
# Quantas letras ao todoq sem considerar espaços e quantas eletras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()# vai excluir os espaços do lado esquerdo e direito.
print('Analisador seu Nome...')
print('Seu nome em Maiúsculo é',nome.upper())
print('Seu nome em Minúsculo é',nome.lower())
print('Seu nome em todo',len(nome) - nome.count(' '),'Letras') #dessa forma vai eliminar o espaço que damos dentro do a pos o primeiro nome e proximo.
print('A frase tem' ,nome.find(' '))
