#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
#https://youtu.be/9dlBZlkvvxY

n = int(input('Digite um numero: '))
f = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end = '')
    print(' x ' if n > 1 else ' = ', end = '')
    f *= n
    n -= 1
print('{}'.format(f))