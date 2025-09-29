#029 - Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,oo reias por cada Km acima do limite.

velocida = float(input('velocidade do Carro ? '))
limite = 80
reais = 7
multa = velocida-limite
multa = multa * reais
print(multa) # mostra o calculo da multa


if velocida > limite:
    print('Você foi Multado em R$ {} Reais pois estava acima de {}Km/h.'.format(multa,limite))
else:
    print('')


