#031 - Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem,cobrado R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a Distancia da viagem em Km ? '))
limite = 200
cobrado = 0,50
multa = velocida-limite
multa = multa * cobrado
print(multa) # mostra o calculo da multa


if velocida == limite:
    print('Você foi Multado em R$ {} Reais pois estava acima de {}Km/h.'.format(multa,limite))
else:
    print('')