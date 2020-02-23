#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
#https://youtu.be/mYlbttiLHM0


n = int(input('Digite um numero:[999 para parar]: '))
soma = 0
cont = 0

while n != 999:
    soma+= n
    cont+= 1
    n = int(input('Digite um numero:[999 para parar]: '))

print('A soma dos numeros digitados foi: {}'.format(soma))


print('Foram introduzidos {} números'.format(cont))