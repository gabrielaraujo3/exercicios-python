n1 = float(input('Valor do produto: R$'))
print('''Escolha a forma de pagamento:
[ 1 ] Á vista (dinheiro/cheque) com 10%off
[ 2 ] Á vista no cartão com  5%off
[ 3 ] 2x no cartão sem juros
[ 4 ] 3x ou mais no cartão com 20% de juros.''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    d = n1 - (n1 * 0.10)
    print(f'Você receberá 10% de desconto e pagará R${d:.2f}')
elif opcao == 2:
    d = n1 - (n1 * 0.05)
    print(f'Você receberá 5% de desconto e pagará R${d:.2f}')
elif opcao == 3:
    print(f'Você pagará o valor normal do produto R${n1:.2f}')
elif opcao == 4:
    j = n1 + (n1 * 0.20)
    print(f'Você pagará R${j:.2f}')
else:
    print('Opção inválida. Tente novamente')