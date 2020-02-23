#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
#https://youtu.be/iHjsUxNA-wo

n = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        n += c

print('A soma de todos {} valores solicitados é {}'.format(cont, n))