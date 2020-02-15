#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
#https://youtu.be/PGqHyzWoagc

N = int(input('Digite a distancia da sua viage'))

if N <= 200:
    print('Valor da passagem: R$ {:.2f}'.format(N*0.50))
else:
    print('Valor da passagem: R$ {:.2f}'.format(N*0.45))