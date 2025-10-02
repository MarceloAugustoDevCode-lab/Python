#048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
contador = 0
soma = 0
for c in range(1,500,2):
    if c %3 == 0:
        contador = contador + 1
        soma = soma + c
print(f'A Soma de todos os \033[1;34;40m{contador}\033[m valores solicitados é \033[1;34;40m{soma}\033[m', end=' ')