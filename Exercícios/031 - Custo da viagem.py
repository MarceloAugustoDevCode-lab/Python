#031 - Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem,cobrado R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Qual a Distancia da viagem em Km ? '))
limite = 200
cobrado = distancia * 0.50
cobrado2 = distancia * 0.45

if distancia <= limite:
    print('Você foi cobrado em R${} pelo distancia {}Km/h.'.format(cobrado,distancia))
else:
    print('Você foi cobrado em R${} pelo distancia {}Km/h.'.format(cobrado2,distancia))