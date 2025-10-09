#061 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print(30*'=')
print(' 10 Termos de PA ')
print(30*'=')

primeirotermo = int(input('Primeiro Termo: '))
razao =int(input('Razao: '))
decimo = primeirotermo + (10 - 1)* razao
for c in range(primeirotermo,decimo + razao,razao):
    print(c,'>',end=' ')
print('ACABOU!!!')
#imcompleto