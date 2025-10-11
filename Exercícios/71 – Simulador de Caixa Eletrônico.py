#071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


contagem = 0
cedulas1 = 1
cedulas10 = 10
cedulas20 = 20
cedulas50 = 50
valor = 0

print(30*"=")
print("CAIXA ELETRONICO")
print(30*"=")

contagem += 1
valor = int(input("Digite o valor do saque? R$ "))
resto1 = valor // cedulas50
print(resto1)

resto2 = resto1
resto2 = resto1 // cedulas20
print(resto2)

resto3 = resto2
resto3 = resto2 // cedulas10
print(resto3)

resto4 = resto3
resto4 = resto3 // cedulas1
print(resto4)




print(f'Total de {resto1} cedulas de R$ 50')
print(f'Total de {resto2} cedulas de R$ 20')
print(f'Total de {resto3} cedulas de R$ 10')
print(f'Total de {resto4} cedulas de R$ 1')


