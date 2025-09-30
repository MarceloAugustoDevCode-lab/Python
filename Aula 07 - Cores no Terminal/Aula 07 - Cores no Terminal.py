#Aula 07 — Cores no terminal.

#estude o modulo colorsys

#ANSI
#ESCAPE SEQUENCE
#style codigos melhores para o python, 0 none ,1 negrito ,4 sublinhado ,7 negative
#cores texto, 30 branco ,31 vermelho ,32 verde ,33 amarelo ,34 azul ,35 roxo ,36 azul claro ,37 cinza.
#Background, 40 branco ,41 vermelho ,42 verde ,43 amarelo ,44 azul ,45 roxo ,46 azul claro ,47 cinza.

#\033[stilo da fonte , cor da texto,background a cor do fundo,m
print('\033[1;32;40m Ola Mundo! \033[m')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[31m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}


a= int(input('Digite o primeito numero: '))
b= int(input('Digite o segundo numero: '))
soma = a + b



# lembrando que não dar espaços entre fim e o início da outra. a melhor e essa
print('\033[7;30;47m Os valores são\033[m','\033[1;31;40m',a,' + ',b,'=',soma,'\033[m')
#ou
#print('Os valores são {}{}{} e {}{}{} são a soma {}{}{}'.format(cores['vermelho'],a,cores['vermelho'],cores['vermelho'],b,cores['vermelho'],cores['vermelho'],soma,cores['vermelho']))
#ou
#print('Os valores são {}{}{} e {}{}{}  são a soma {}{}{}'.format('\033[1;31;40m',a,'\033[m','\033[1;31;40m',b,'\033[m','\033[1;31;40m',soma,'\033[m'))
#ou
#print('\033[7;30;47m Os valores são \033[m\033[1;31;40m {} e {} \033[7;30;47m são a soma \033[m\033[1;31;40m{}\033[m'.format(a,b,soma))
