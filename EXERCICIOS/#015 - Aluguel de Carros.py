#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#https://youtu.be/I4NYUeetLAc

KM = float(input('Digite os kilometros rodados: '))
DIAS = int(input('Por quantos dias o carro foi utilizado: '))

CUSTOKM = KM*0.15
DIARIA = DIAS * 60
TOTAL = CUSTOKM + DIARIA

print('O total a pagar pelo aluguel do carro é: R$ {:.2f}' .format((TOTAL)))