#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#https://youtu.be/9GvsphwW26k

import math

N = int(input('Digite o angulo: '))

R = math.radians(N)

print('COS = {:.3f} SEN = {:.3f} TAN = {:.3f}'.format(math.cos(R), math.sin(R), math.tan(R)))

