salario = float(input('Digite o valor do sálario? R$'))
if salario>1250.00:
    print('O novo sálario com aumento é R${:.2f}'.format((salario*0.10)+salario))
else:
    print('O novo sálario com aumento é R${:.2f}'.format((salario*0.15)+salario))
