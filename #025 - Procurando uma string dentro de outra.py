#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#https://youtu.be/WHWGz2Dy1ZU

N = str(input('Digite seu nome: ')).strip()

print('Seu nome tem Silva? {}' .format('SILVA' in N.upper()))