#018
# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse angulo.
import math

angulo = float(input('Digite o o valor do ângulo? '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {}, valor de seno {:.2f} de Cosseno {:.2f} e do Tangente {:.2f} '.format(angulo,seno, coseno, tangente))

