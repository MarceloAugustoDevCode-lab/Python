#035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento do primeira reta: '))
r2 = float(input('Digite o comprimento do segunda reta: '))
r3 = float(input('Digite o comprimento do terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima podem formar um triângulo.. sim')
else:
    print('Os segmentos acima não podem formar um triângulo.')




