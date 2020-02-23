#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#https://youtu.be/SifYYsXhLM8

N = str(input('Digite seu nome completo: ')).upper().strip()

nome = N.split()

print('Primeiro: {}'.format(nome[0]))
print('Ultimo: {}'.format(nome[len(nome)-1]))
