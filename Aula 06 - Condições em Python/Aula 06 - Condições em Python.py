#estrutura de sequencia: condicionais.

#vou explicar de modo rapido. primeiro vou criar uma variavel com nome de nome:
nome = input('Digite seu nome: ')
# depois criar outra variavel com nome de escolha para dar a função do if(se) e else(senão)
escolha = input('escolha se maiúsculo ou minúsculo se nao aperte enter: ')

#se eu quero que nome fique Maiúsculo o vou escrever maiúsculo , if no python e (se).
if escolha == 'maiúsculo':# se escolha for (==) igual string 'maiúsculo' ficara maiúsculo
    print(nome.upper())#função que altera para maiúsculo

#senão eu quero que nome fique Minúsculo o vou escrever qualquer outra se Minúsculo, else no python e (senão).
else:#senão a escolha sera minúsculo
    print(nome.lower())#função que altera para minúsculo

'''
tempo = int(input('Quantos anos tem seu carro ? '))

if tempo <= 3 :
    print('carro novo')
else:
    print('carro carro velho')
print('--FIM--')
'''

#ou

'''
tempo = int(input('Quantos anos tem seu carro ? '))
print('carro novo'if tempo <=3 else 'carro velho'))
print('--FIM--')
'''


