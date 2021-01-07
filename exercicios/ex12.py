n1 = float(input('Valor do produto (R$): '))
n2 = float(input('Desconto em porcentagem (%): '))
d = n2/100
d1 = n1*d
nv = n1-d1
print('Novo valor do produto com {}% de desconto: R${:.2f}'.format(n2,nv))
