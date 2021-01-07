n = int(input('Informe um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhar(es).'.format(n, n2[1]))
print('O número {} possui, {} centena(s)'.format(n, n2[2]))
print('O número {} possui, {} dezena(s)'.format(n, n2[3]))
print('O número {} possui, {} unidade(s)'.format(n, n2[4]))

#print('O número {} possui: {} milhar(es), {} centena(s), {} dezena(s) e {} unidade(s).'.format(n, n2[1], n2[2],
#n2[3], n2[4]))
