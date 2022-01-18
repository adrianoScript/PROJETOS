" Um programa que faça o computador jogar Jokenpô com você."
from random import randint
from time import sleep
intes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print("""Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura""")
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=='*12)
print(f'Computador jogou: {intes[computador]}')
print(f'Jogador jogou: {intes[jogador]}')
print('=='*12)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
       print('Empate') 
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Inválida!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida!')