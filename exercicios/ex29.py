n1 = int(input('Velocidade do carro: '))
if n1 <= 80:
    print('Boa viagem!')
else:
    print('Você foi multado! Limite de 80km/h.')
    print('Valor da multa R${:.2f}'.format((n1-80)*7))
