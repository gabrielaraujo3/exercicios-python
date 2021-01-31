from time import sleep
print('= ' * 26)
sleep(0.5)
print('{:^52}'.format('BANCO CEV'))
sleep(0.3)
print('= ' * 26)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
print('Analisando a transação...')
sleep(1)
print('Verificando a disponibilidade de cédulas...')
for c in range(1, 26):
    print('= ', end='')
    sleep(0.20)
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
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            cont = 0
            if total == 0:
                break
else:
    total = total - 5
    print('\nTotal de 1 cédula de R$5')
    sleep(0.5)
    while True:
        if total >= ced:
            total -= ced
            cont += 1
        else:
            if cont > 0:
                print(f'Total de {cont} cédulas de R${ced}')
                sleep(0.5)
            elif ced == 200:
                ced = 100
            elif ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 2
            cont = 0
            if total == 0:
                break
for c in range(1, 26):
    print('= ', end='')
    sleep(0.20)
sleep(0.5)
print('\nRetire seu dinheiro...')
for c in range(1, 26):
    print('= ', end='')
    sleep(0.20)
sleep(0.5)
print('\nEncerrando...')
for c in range(1, 26):
    print('= ', end='')
    sleep(0.20)
sleep(0.5)
print('\nVolte sempre ao BANCO CEV! Tenha um bom dia!')
#valores com 8 na composição nao são compativeis por causa da ordem de seleção das notas, resolverei na proxima versão.