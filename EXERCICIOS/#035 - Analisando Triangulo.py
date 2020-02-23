#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#https://youtu.be/NZiNphKkxhg
#Adicionar cores

a = float(input(('Digite o valor de A: ')))
b = float(input(('Digite o valor de B: ')))
c = float(input(('Digite o valor de C: ')))

if a < b+c and b < a+c and c < b+a:
    print('Este conjunto pode formar um \033[1;32mTriangulo \033[m')
else:
    print('Este conjunto não pode formar um \033[1;31mTriangulo \033[m')