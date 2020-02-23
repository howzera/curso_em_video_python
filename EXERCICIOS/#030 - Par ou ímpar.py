#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#https://youtu.be/4vFCzKuHOn4

N = int(input('Digite um numero:'))

if (N % 2) == 0:
    print('O numero digitado é par')
else:
    print('O numero digitado é impar')