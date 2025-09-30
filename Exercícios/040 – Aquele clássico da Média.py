#040 - Cria um programa que laia duas notas de um aluno a calcula sua média, mostrando uma mansagem no final. da acordo com a média atingida:
#- Média abaixo da 5.0:REPROVADO
#- Média entra 5.0 a 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior:APROVADO

nota = int(input('Digite sua Primeira Nota: '))
nota2 = int(input('Digite sua Segunda Nota: '))

media = (nota + nota2) / 2

if media >= 7:
    print('\033[1;31;40mAPROVADO {}\033[m'.format(media))
elif media == 5 and media < 6.9:
    print('\033[1;31;40mRECUPERAÇÃO {}\033[m'.format(media))
elif media < 5:
    print('\033[1;31;40mREPROVADO {}\033[m'.format(media))