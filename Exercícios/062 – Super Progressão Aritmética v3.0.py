#062 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print(30*'=')
print(' 10 Termos de PA ')
print(30*'=')

primeirotermo = int(input('Primeiro Termo: '))
razao =int(input('Razao: '))
decimo = primeirotermo + (10 - 1)* razao


# Progressão aritmética com while (exemplo: 2, 4, 6, ..., 10)
contador = 1
termo = primeirotermo
total = 0
mais = 10# Número de termos
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo,end=' ')
        termo += razao
        contador += 1
    print('Pausa !!!')
    mais = int(input('Quantos termos você quer mostrar a mais:  '))

print(f' total de termos finalizados {total}')