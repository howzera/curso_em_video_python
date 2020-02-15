#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#https://youtu.be/9l_Gay8BuAw
#Adicionar cores

C = float(input('\033[1mInforme a temperatura em ºC:\033[36m '))
print('\033[m')
F = ((9 * C) / 5) +32
print('\033[1;4mA temperatura de \033[36m{}ºC\033[m \033[1;4mcorresponde a \033[31m{}ºF'.format(C,F))
print('\033[m')