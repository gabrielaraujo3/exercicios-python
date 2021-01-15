print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Valor do produto: R$'))
print('''Escolha a forma de pagamento:
[ 1 ] Á vista (dinheiro/cheque) com 10%off
[ 2 ] Á vista no cartão com  5%off
[ 3 ] 2x no cartão sem juros
[ 4 ] 3x ou mais no cartão com 20% de juros.''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total /2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
