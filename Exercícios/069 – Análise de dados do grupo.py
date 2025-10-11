# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
homem = 0
mulher = 0
total = 0
continuar = 'S'

while True:
    print(30 * '-')
    print('CADASTRE UMA PESSOA')
    print(30 * '-')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem +=1
    if sexo == 'F' and idade < 20:
        mulher +=1
    if idade > 18:
        total +=1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(30 * '-')
print(f'Total de pessoas cadastradas com mais de 18 anos: {total}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')