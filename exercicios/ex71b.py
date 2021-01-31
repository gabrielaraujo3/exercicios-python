from random import randint
from time import sleep
from datetime import datetime
agora = datetime.now()


while True:
    print('= ' * 26)
    sleep(0.2)
    print('{:^52}'.format('BANCO CEV'))
    sleep(0.2)
    print('= ' * 26)
#    valor = int(input('Que valor você quer sacar? R$'))
    valor = randint(1, 5000)
    print(f'Valor do saque R${valor}')
    total = valor
    print('Analisando a transação...')
    sleep(0.5)
    print('Verificando a disponibilidade de cédulas...')
    for c in range(1, 26):
        print('= ', end='')
        sleep(0.10)
    ced = 200
    cont = 0
    if total % 2 == 0:
        while True:
            if total >= ced:
                total -= ced
                cont += 1
            else:
                if cont > 0:
                    print(f'\nTotal de {cont} cédulas de {ced}')
                    sleep(0.5)
                if ced == 200:
                    ced = 100
                elif ced == 100:
                    ced = 50
                elif ced == 50:
                    ced = 20
                elif ced == 20:
                    if total % 5 == 1:
                        ced = 2
                    else:
                        ced = 10
                elif ced == 10:
                    if total % 4 == 0:
                        ced = 2
                    elif total % 5 != 0:
                        ced = 2
                    else:
                        ced = 5
                elif ced == 5:
                    ced = 2
                cont = 0
                if total == 0:
                    break
    else:
        total = total - 5
        print('\nTotal de 1 cédula de R$5')
        sleep(0.2)
        while True:
            if total >= ced:
                total -= ced
                cont += 1
            else:
                if cont > 0:
                    print(f'\nTotal de {cont} cédulas de R${ced}')
                    sleep(0.5)
                elif ced == 200:
                    ced = 100
                elif ced == 100:
                    ced = 50
                elif ced == 50:
                    ced = 20
                elif ced == 20:
                    if total % 5 != 0:
                        ced = 2
                    else:
                        ced = 10
                elif ced == 10:
                    if total % 4 == 0:
                        ced = 2
                    elif total % 5 != 0:
                        ced = 2
                elif ced == 5:
                    ced = 2
                cont = 0
                if total == 0:
                    break
    for c in range(1, 26):
        print('= ', end='')
        sleep(0.20)
    sleep(0.2)
    print('\nRetire seu dinheiro...')
    sleep(0.2)
    print('\nEncerrando...')
    for c in range(1, 26):
        print('= ', end='')
        sleep(0.2)
    sleep(0.2)
    print('\nVolte sempre ao BANCO CEV! Tenha um bom dia!')
# codigo muito grande desnecessariamente, com muita coisa repetida,
# melhorarei isso na proxima versão.