#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#https://youtu.be/4MAmKOT9FeU
#Adicionar cores

N = float(input('Digite o valor do produto: \033[4;31mR$ '))

print('\033[m')

DESCONTO = N*0.95

print('\033[1mO valor com desconto é:\033[1;4;32mR$ {:.2F}\033[m'.format(DESCONTO))