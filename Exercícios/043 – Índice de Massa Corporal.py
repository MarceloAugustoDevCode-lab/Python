#043 - Desenvolva uma lógica que laia o paso a a altura da uma pessoa.calcule seu IMC a mostre seu status. de acordo com a tabela abaixo:
#- Abaixo da 18.5: Abaixo do Paso
#- Entre 18.5 a 25: Paso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidada
#Acima de 40: Obesidada mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
print('O IMC desse pessoa é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Paso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')