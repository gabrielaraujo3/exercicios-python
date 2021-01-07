print('\033[4;34mBem vindo!\033[m \033[32;1mAqui você consegue seu empréstimo para a compra da casa própria!!\033[m')
valor = float(input('Valor da casa a ser financiada: R$'))
salario = float(input('Qual o salário do comprador: R$'))
anos = int(input('Em quantos anos pretende pagar: '))
parcelas = valor / (anos * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, parcelas))
if parcelas <= minimo:
    print('PARABÉNS! Seu empréstimo foi pré-aprovado. Entraremos em contato em breve.')
else:
    print('Infelizmente seu empréstimo não foi aprovado, sentimos muito e pedimos que tente novamente daqui a 30 \n'
          'dias.')