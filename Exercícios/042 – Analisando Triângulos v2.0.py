#042 - Rafaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo sará formado:
#- Equilátero: todos os lados iguais
#-Isóscales: dois lados iguais
#-Escalano: todos os lados diferentes

reta1 = float(input('Digite o comprimento do primeira reta: '))
reta2 = float(input('Digite o comprimento do segunda reta: '))
reta3 = float(input('Digite o comprimento do terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Os segmentos acima podem formar um triângulo.. sim')
    if reta1 == reta2 == reta3:
        print('Esse Triângulo é Equilátero:')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse Triângulo é Isósceles:')
    else:
        print('Esse Triângulo é Escaleno:')
else:
    print('Os segmentos acima não podem formar um triângulo.')