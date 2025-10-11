#071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


contagem = 0
cedulas1 = 1
cedulas10 = 10
cedulas50 = 50
valor = 0
print(30*"=")
print("CAIXA ELETRONICO")
print(30*"=")


contagem += 1
total = contagem + valor
valor = int(input("Digite o valor do saque? R$ "))
if total == valor :
    contagem += 1
    cedulas50 += 50
    print(f'Total de {contagem} cedulas de R$ {cedulas50}')


