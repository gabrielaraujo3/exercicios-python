n1 = float(input('Quantos metros de altura a parede tem: '))
n2 = float(input('E de largura: '))
a = n1*n2
t = a/2
print ('O total da área é {}m2, considerando que cada litro de tinta pinte 2x2m, \n'
       'você precisara de {:.3f}L de Tinta.'.format(a,t))
