#059 - Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.



escolha = 's'
while escolha != 'n':
    print(30*'=')
    print('''
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos numeros
        [5]sair do programa
    ''')
    print(30*'=')
    escolha = str(input('Digite o numero de sua preferencia: ')).strip().upper()[0]
    if escolha == '5':
        print('Obrigado por utilizar o programa')
        escolha = 'n'
    elif escolha == '4':
        print('Escolha novamente: ')
        primeiro = int(input('Digite o primeiro numero: '))
        segundo = int(input('Digite o segundo numero: '))
    else:
        #soma
        if escolha == '1':
            primeiro = int(input('Digite o primeiro numero: '))
            segundo = int(input('Digite o segundo numero: '))
            soma = primeiro + segundo
            print(f'A soma dos numeros: {soma}')
        #multiplicação
        if escolha == '2':
            primeiro = int(input('Digite o primeiro numero: '))
            segundo = int(input('Digite o segundo numero: '))
            multiplicador = primeiro * segundo
            print(f'A Multiplicação dos numeros: {multiplicador}')
        #uma e maior que outro
        if escolha == '3':
            maior =0
            primeiro = int(input('Digite o primeiro numero: '))
            segundo = int(input('Digite o segundo numero: '))
            if primeiro > segundo:
                print('O primeiro numero e maior que o segundo numero')
            else:
                print('O segundo numero e maior que o primeiro numero')
        #Continua
        if escolha == 'n':
            print('O programa terminou com sucesso')
            escolha = 'n'
