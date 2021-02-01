from datetime import datetime
#from random import randint
from time import sleep
extrato = 1
resp = ' '
while resp not in 'N':
    resp = ' '
    agora = datetime.now()
    data_hora = agora.strftime('%d/%m/%Y, %H:%M:%S')
    valor = 0
    sleep(0.5)
    print('= ' * 26)
    sleep(0.3)
    print('{:<4}{:<6}{:^21}{:>18}'.format('EXT ', extrato, 'BANCO CEV', data_hora))
    sleep(0.2)
    print('= ' * 26)
    print('Notas disponíveis neste caixa:')
    print('R$2, R$5, R$10, R$20, R$50, R$100 e R$200\n')
    print('Valor mínimo por saque:')
    print('R$5')
    print('* ' * 26)
    while valor < 5:
        valor = int(input('Que valor você quer sacar? R$'))
        #valor = randint(1, 5000)
        print(f'Valor do Saque R${valor}')
    total = valor
    print('Analisando a transação...')
    sleep(0.5)
    print('Verificando a disponibilidade de cédulas...')
    sleep(0.5)
    print('Contando...')
    sleep(1)
    for c in range(1, 27):
        print('= ', end='')
        sleep(0.3)
    ced = 200
    cont = 0
    menos5 = 0
    while total % 2 != 0:
        total -= 5
        menos5 += 1
        if menos5 > 0:
            print(f'\nTotal de {menos5} cedulas de R$5')
            sleep(0.5)
    while True:
        if total >= ced:
            total -= ced
            cont += 1
        else:
            if cont > 0:
                print(f'\nTotal de {cont} cédulas de R${ced}')
                sleep(0.5)
            if ced == 200:
                ced = 100
            elif ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                if total % 4 == 0:
                    ced = 2
                elif total == 6:
                    ced = 2
                else:
                    ced = 2
            elif ced == 5:
                ced = 2
            cont = 0
            if total == 0:
                extrato += 1
                break
    for c in range(1, 27):
        print('= ', end='')
        sleep(0.3)
    print('\nRetire seu dinheiro...')
    sleep(1)
    while resp not in 'SN':
        resp = str(input('Deseja fazer mais um saque [S/N]? ')).strip().upper()[0]
print('\nEncerrando...')
for c in range(1, 27):
    print('= ', end='')
    sleep(0.3)
#    sleep(0.25)
print('\n{:^52}'.format('Volte sempre ao BANCO CEV! Tenha um bom dia!'))
    # pronto, acho que não consigo melhorar nada mais(talvez umas cores mais tarde)