#061 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print(30*'=')
print(' 10 Termos de PA ')
print(30*'=')

primeirotermo = int(input('Primeiro Termo: '))
razao =int(input('Razao: '))
decimo = primeirotermo + (10 - 1)* razao


# Progressão aritmética com while (exemplo: 2, 4, 6, ..., 10)
n = 10   # Número de termos
contador = 1
termo = primeirotermo
while contador <= n: #contador é menor e igual n.
    print(termo,end=' ')
    termo += razao
    contador += 1
print('FIM!!!')