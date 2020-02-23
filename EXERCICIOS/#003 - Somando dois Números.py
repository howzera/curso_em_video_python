#Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.
#https://youtu.be/PB254Cfjlyk
#Adicionar cores

N1 = int(input('Digite o valor de N1: '))
N2 = int(input('Digite o valor de N2: '))
R = N1 + N2
print('\033[1;31;40m{}\033[m'.format(R))