# Desafio 011

#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2quadrado.

largura = int(input('Digite a largura ? '))
altura = int(input('Digite a altura ? '))
extra = int(input('Se houver portas ou janelas, calcule e some e coloque Aqui ? '))

total = (largura * altura) - extra
print(total)
area = total/2
demaos = area * 2
print('Sabendo que 1 litro de tinta pinta 2m², Calculo da quantidade de tinta necessária é {} litros de tinta e se for 2 demãos é {} litros de tinta'.format(area,demaos))
