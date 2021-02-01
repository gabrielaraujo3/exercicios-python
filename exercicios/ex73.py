times = ('Internacional', 'Atlético-MG', 'Flamengo', 'São Paulo', 'Fluminense',
         'Palmeiras', 'Grêmio', 'Athletico-PR', 'Ceará SC', 'Corinthians', 'Santos',
         'Atlético-GO', 'Bragantino', 'Vasco da Gama', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Goiás', 'Coritiba', 'Botafogo')
print('=-' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('=-' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('=-' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Athletico-PR está na {times.index("Athletico-PR")+1}ª posição')