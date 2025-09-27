#027 - Crie um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#ex ana maria de souza
#primeiro = ana
#ultimo = souza

#marcelo augusto de jesus

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.upper()
nome = nome.split()
print('O Primeiro nome é ',nome[0])
print('O Segundo nome é',nome[1])