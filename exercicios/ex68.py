from random import randint
computador = randint(0, 10)
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
venceu = 0
while True:
    jogador = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 40)
    s = computador + jogador
    if s % 2 == 0:
        if pi == 'P':
            venceu += 1
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif pi == 'I':
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR')
            print('-' * 40)
            print('Você PERDEU!')
            break
    if s % 2 != 0:
        if pi == 'P':
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU ÍMPAR')
            print('-' * 40)
            print('Você PERDEU!')
            break
        elif pi == 'I':
            venceu += 1
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU ÍMPAR')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
print('=-' * 20)
if venceu == 0:
    print('GAME OVER!')
elif venceu == 1:
    print(f'GAME OVER! Você venceu {venceu} vez')
else:
    print(f'GAME OVER! Você venceu {venceu} vezes')