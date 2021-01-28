mais18 = homens = mulher20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulher20 += 1
    if mais == 'N':
        print('===== FIM DO PROGRAMA =====')
        break
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homens cadastrados
E temos {mulher20} mulheres com menos de 20 anos.''')



