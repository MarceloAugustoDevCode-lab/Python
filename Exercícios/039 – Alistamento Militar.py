#039 - Faça um programa qua laia o ano da nascimento da um jovem a informa.da acordo com sua idade:
#- Sa ala ainda vai se alistar ao serviço militar.
#-Sa é a hora de se alistar.
#-Sa já passou do tempo do alistamento.
#Sau programa também davará mostrar o tampo que falta ou que passou do prazo.

import datetime

data = datetime.date.today().year
print(data)
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = data - nascimento



if nascimento == 18:
    print('Quem nasceu em {} e tem {} anos, o Seu alistamento e agora!!! {}'.format(nascimento,idade, data))
elif nascimento < 18:
    saldo = 18 - idade
    print('Quem nasceu em {} e tem {} anos ,Seu alistamento vai ser em {}.'.format(nascimento,idade ,saldo))
elif nascimento > 18:
    saldo = idade - 18
    print('Seu alistamento foi ja passou!!!')import datetime

# Obtém o ano atual
ano_atual = datetime.date.today().year

# Solicita o ano de nascimento
nascimento = int(input('Digite o ano do seu nascimento: '))

# Calcula a idade
idade = ano_atual - nascimento

# Validação simples do ano de nascimento
if nascimento > ano_atual or nascimento < (ano_atual - 100):
    print('Ano de nascimento inválido! Por favor, insira um ano válido.')
else:
    if idade == 18:
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print('É hora de se alistar ao serviço militar!')
    elif idade < 18:
        saldo = 18 - idade
        ano_alistamento = ano_atual + saldo
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')
    else:  # idade > 18
        saldo = idade - 18
        ano_alistamento = ano_atual - saldo
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print(f'Seu alistamento já passou! Deveria ter sido há {saldo} ano(s), em {ano_alistamento}.')


