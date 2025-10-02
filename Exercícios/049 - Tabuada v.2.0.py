#049 - Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um numero para ver sua tabuada: '))
for c in range(0,11):
    numero = numero
    multiplicacao = c * numero
    print(f'{numero}x{c} = {multiplicacao}')

#ou
print('\033[1;34;40mFIM\033[m')
for c in range(0,11):
    print(f'{numero}x{c} = {numero * c}')
