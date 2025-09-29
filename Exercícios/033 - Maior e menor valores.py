#033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))


#verifica menor
if numero < numero2:
    print('O menor valor digitado! {}'.format(numero))
elif numero2 < numero3:
    print('O menor valor digitado! {}'.format(numero2))
else:
    print('O menor valor digitado! {}'.format(numero3))

#verifica maior
if numero > numero2:
    print('O maior valor digitado! {}'.format(numero))
elif numero2 > numero3:
    print('O maior valor digitado! {}'.format(numero2))
else:
    print('O maior valor digitado! {}'.format(numero3))

#ou
'''
#verifica menor
menor = numero
if numero2 < numero and numero2 < numero3:
    menor = numero2
if numero3 < numero and numero3 < numero2:
    menor = numero3
    
#verifica maior
maior = numero
if numero2 > numero and numero2 > numero3:
    maior = numero2
if numero3 > numero and numero3 > numero2:
    maior = numero3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''