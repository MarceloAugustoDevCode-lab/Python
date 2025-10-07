#56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
c =0
media = 0
for c in range(1,2+1): # inicio, fim, passo:
    nome = str(input(f'Digite o nome {c}° Pessoa: ')).strip().upper()
    idade = int(input(f'Digite o a Idade da {c}° pessoa: '))
    sexo = str(input(f'Digite o sexo (M/F): ')).strip().upper()
    # media do grupo
    media += idade# soma os numeros idade
    # homem mais velho
    if c ==1 or idade > idade:
        nomev = nome
        idadev = idade
        sexov = sexo
    vnome = nomev
    vidade = idadev
    vsexo = sexov
media1 = media / 4 #divide os numeros da media.
print(f'O homem mais velho e {nomev} tem {idadev} anos e do sexo {vsexo}. ')
print(f'Qual e a Media do grupo: {media1}')