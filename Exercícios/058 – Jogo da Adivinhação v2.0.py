#058 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
acerto = 0
palpites = 0

print(20*'-','Jogo da Adivinhação',20*'-')
print('Regras quem tiver mais palpites perde, adivinhe 1 a 10')
while acerto != 1:
    adivinha = random.randint(1,10)
    print(adivinha)
    acerto = int(input('Digite o numero do seu palpite: '))
    if acerto == adivinha:
        print(f'O numero de palpites foram {palpites}, parabens você venceu!')
        acerto = 1
    else:
        palpites += 1
