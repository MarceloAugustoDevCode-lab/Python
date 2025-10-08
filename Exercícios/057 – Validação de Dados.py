#057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
#a minha solução:
'''
para = 'S'
contador = 0
while para == 'S':
    contador += 1
    sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
    if sexo == 'M'or sexo == 'F':
        print(f'O sexo da {contador}° Pessoa é {sexo}')
    else:
        print('Digite um valor valido!')
    para = str(input('Deseja  continuar? [S/N]: ')).strip().upper()[0]
    if para not in 'S':
        print('Você fechou o programa')
        para == 'S'
    else:
        print('Continue!')
'''
#ou


sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite os dados corretos, Por favor informe seu sexo:[M/F]: ')).strip().upper()[0]
print(f'sexo: {sexo} Registrado com sucesso!')
