from random import randint

v = 0
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in 'PI':
        tipo = str(input('Par ou Impa [P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e computador {computador} e total {total}')
    print('deu PAR' if total % 2 == 0 else 'deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')
