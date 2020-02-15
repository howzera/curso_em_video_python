#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#https://youtu.be/vmPW9iWsYkY
import math

N1 = int(input('Digite  o valor do cateto adjacente: '))
N2 = int(input('Digite o valor do cateto oposto: '))

print('O valor da Hypotenusa é {:.2f}'.format(math.hypot(N1,N2)))