#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#https://youtu.be/qajq3SI0QQs
#Adicionar cores

N = float(input('Qual o valor deseja converter:\033[1;36m '))

DOLAR = N/3.27

print('Com R$ {:.2f} é possível comprar U$ {:.2F}'.format(N, DOLAR))