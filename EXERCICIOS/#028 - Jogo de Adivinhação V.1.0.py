#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#https://youtu.be/kchC5KLZSZ4

from random import randint

n = randint(0, 5)

s = int(input('Digite um numero: '))

if s == n:
    print('Parabéns, você acertou o numero')
else:
    print('Infelizmente você errou')
