#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
#https://youtu.be/hgJ_ETNGSj8

N = int(input('Digite a velocidade do carro: '))

if N > 80:

    S = N - 80
    print('Você foi multado: R$ {:.2f}'.format(S*7.00))