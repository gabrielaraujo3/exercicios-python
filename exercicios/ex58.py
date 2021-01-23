from random import randint
from time import sleep
pc = randint(0, 10)
tentativas = 1
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(0.2)
while pc != jogador:
    tentativas += 1
    if pc < jogador:
        jogador = (int(input('Menos... Tente novamente: ')))
        print('Processando...')
        sleep(0.2)
    elif pc > jogador:
        jogador = (int(input('Mais... Tente novamente: ')))
        print('Processando...')
        sleep(0.2)
print(f'Parabéns! O número que pensei foi {pc}, você precisou de {tentativas} tentativas.')
