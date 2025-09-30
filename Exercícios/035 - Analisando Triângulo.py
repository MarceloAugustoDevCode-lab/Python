#035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimento do primeira reta: '))
reta2 = float(input('Digite o comprimento do segunda reta: '))
reta3 = float(input('Digite o comprimento do terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Os segmentos acima podem formar um triângulo.. sim')
else:
    print('Os segmentos acima não podem formar um triângulo.')




