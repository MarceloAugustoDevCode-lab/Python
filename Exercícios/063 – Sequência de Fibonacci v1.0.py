#063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0     –   1   –   1   – 2 – 3 – 5 – 8
#termo - termo2

contagem = 0
termo = 0
termo2 =1
numero = int(input('Quantos termos você quer mostrar: '))
while contagem <= numero-1:
    fibonacci = termo + termo2
    termo = termo2
    termo2 = fibonacci
    contagem += 1
    print(f'{fibonacci} ', end=' ')
print('Fim!!!')

