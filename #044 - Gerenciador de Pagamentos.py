#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
#https://youtu.be/I-SH3QchuZ4

n = float(input('Digite o valor do produto: R$\033[1;31m'))

print('\033[m')

print("""\033[1mQual a opção de pagamento?\n
    1 - A VISTA NO DINHEIRO ou CHEQUE
    2 - A VISTA NO CARTÃO
    3 - EM ATÉ 2x NO CARTÃO
    4 - 3x ou mais no cartão
""")
pagamento = int(input('Digite uma das opções: '))


if pagamento == 1:
    print('O valor para pagamento a vista é \033[1;32m R$ {} '.format(n*0.95))
elif pagamento == 2:
    print('O valor para pagamento a vista no cartão é \033[1;32m R$ {} '.format(n*0.90))
elif pagamento == 3:
    print('O valor para pagamento em até 2x no cartão é \033[1;32m R$ {} '.format(n))
elif pagamento == 4:
    print('O valor para pagamento no cartão de 3x ou mais é \033[1;32m R$ {} '.format(n*1.20))
else:
    print('\033[1;31MOpção inválida!!!')