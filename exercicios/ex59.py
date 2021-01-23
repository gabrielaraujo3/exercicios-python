from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma opção da lista para prosseguir ou sair:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}')
        print('=-=' * 20)
    if opcao == 2:
        print(f'{n1} multplicado por {n2} é igual a {n1 * n2}')
        print('=-=' * 20)
    if opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é o Maior.')
            print('=-=' * 20)
        else:
            print(f'O número {n2} é o Maior.')
            print('=-=' * 20)
    if opcao == 4:
        n1 = float(input('Digite um novo número: '))
        n2 = float(input('Segundo novo número: '))
    if opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('PROGRAMA FINALIZADO!')
        print('=-=' * 20)
    else:
        print('=-=' * 20)
        print('Opção inválida. Tente novamente!')
        print('=-=' * 20)