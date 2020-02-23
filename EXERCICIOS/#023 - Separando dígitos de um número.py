#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#https://youtu.be/wD2aerLMBWA

N = int(input('Digite um numero entre 1 e 9990: '))

u = N // 1 % 10
d = N // 10 % 10
c = N // 100 % 10
m = N // 1000 % 10



print('O numero contém {} unidades' .format(u))
print('O numero contém {} dezenas' .format(d))
print('O numero contém {} centenas' .format(c))
print('O numero contém {} Milhar' .format(m))