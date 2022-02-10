from random import randint
computador = randint(0, 10)
print('Computador acabou de pensar em um numero:')
print('Advinha qual numero?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'Maior que {jogador}')
        if jogador > computador:
            print(f'Menor que {jogador}')
print(f'acertou com {palpite} tentativas\nPARABEMS!')