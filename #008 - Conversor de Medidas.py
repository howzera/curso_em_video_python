#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#https://youtu.be/KjcdG05EAZc
#Adicionar cores

N = int(input('Digite um valor em metros: '))

CM= N*100
MM= N*1000

print('A conversão em centimetros é:  | R: \033[1;33m{}\033'.format(CM))
print('A conversão em milímetros é:   | R: \033[1;33m{}\033'.format(MM))

