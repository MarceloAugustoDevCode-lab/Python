#033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))
# primeiro numero
if numero < numero2:
    print('O primeiro numero e menor que o segundo numero!')
elif numero > numero2:
    print('O primeiro numero e maior que o segundo numero!')
elif numero == numero2:
    print('O primeiro numero e igual que o segundo numero!')
if numero < numero3:
    print('O primeiro numero e menor que o terceiro numero!')
elif numero > numero3:
    print('O primeiro numero e maior que o terceiro numero!')
elif numero == numero3:
    print('O primeiro numero e igual que o terceiro numero!')



# segundo numero
if numero2 < numero3:
    print('O segundo numero e menor que o terceiro numero!')
elif numero2 > numero3:
    print('O segundo numero e maior que o terceiro numero!')
elif numero2 == numero3:
    print('O segundo numero e igual que o terceiro numero!')
if numero2 < numero:
    print('O segundo numero e menor que o primeiro numero!')
elif numero2 > numero:
    print('O segundo numero e maior que o primeiro numero!')
elif numero2 == numero:
    print('O segundo numero e igual que o primeiro numero!')





# terceiro numero
if numero3 < numero2:
    print('O terceiro numero e menor que o segundo numero!')
elif numero3 > numero2:
    print('O terceiro numero e maior que o segundo numero!')
elif numero3 == numero2:
    print('O terceiro numero e igual que o segundo numero!')
if numero3 < numero:
    print('O terceiro numero e menor que o primeiro numero!')
elif numero3 > numero:
    print('O terceiro numero e maior que o primeiro numero!')
elif numero3 == numero:
    print('O terceiro numero e igual que o primeiro numero!')
