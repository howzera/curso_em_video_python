#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#https://youtu.be/-iSbDpl5Jhw

import math

N = float(input('Digite um numero real: '))

N = math.floor(N)

print('A  porção inteira do numero digitado é: \n | R: {}'.format(N))