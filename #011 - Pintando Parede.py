#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
#https://youtu.be/mzSJpn9ldt4
#Adicionar cores

L = float(input('Digite a largura:\033[1;32m '))

A = float(input('\033[mDigite a altura:\033[1;31m '))

print('\033[m')

AREA = L*A

TINTA = AREA/2

print('\033[1mSerá necessário \033[1;36m{:.2f}\033[m \033[1mLitros de tinta para pintar a parede com \033[1;32m{} M²\033[m'.format(TINTA, AREA))