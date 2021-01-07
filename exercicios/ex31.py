distancia = int(input('Distancia da viagem em Km: '))
if distancia <=200:
    preco = distancia*0.50
    print('O valor da passagem é R${:.2f}'.format(preco))
else:
    preco2 = distancia*0.45
    print('O valor da passagem é R${:.2f}'.format(preco2))
