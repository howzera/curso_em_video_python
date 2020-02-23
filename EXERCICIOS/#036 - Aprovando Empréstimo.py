#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
#https://youtu.be/IV13X0QOMU8

valor_casa = (float(input('Digite o valor da casa: ')))
salario_comprador = float(input('Salário do comprador: '))
anos_financiamento = int(input('Quantos anos de financiamento? '))
parcela = (valor_casa / anos_financiamento) / 12

print('O valor da casa é R$ {}'.format(valor_casa))
print('E para pagar o valor R$ \033[1;32m{}\033[m em \033[1;32m{}\033[m anos, a parcela será de \033[1;32m{:.2f}'.format(valor_casa, anos_financiamento, parcela))

if parcela > (salario_comprador*0.3):
    print('\033[1;31mVOCÊ NÃO PODE FINANCIAR O IMÓVEL NESSAS CONDIÇÕES, TENTE UMA NOVA SIMULAÇÃO\033[m')
else:
    print('Seu financiamento foi \033[1;32mAPROVADO!!!')