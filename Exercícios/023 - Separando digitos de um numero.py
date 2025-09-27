#023 - Faça um programa que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados.
#ex digite um numero: 1834 unidade:4 , dezena:3 , centena:8 , milhar:1
numero = int(input('Digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {}'.format(numero))
print('{} unidade \n {} Dezena \n {} Centena \n {} milhar \n'.format(u,d,c,m))
#ou
#print(f"Sua string convertida para uma lista de caracteres: {lista}") modo de informa a variavel






