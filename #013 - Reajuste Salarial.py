#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#https://youtu.be/cTkivN8XcJ0
#Adicionar cores


N = float(input('Digite seu salário:\033[1;35mR$ '))

print('\033[m')

BONUS = N*1.15

print('\033[1mSeu novo salário é: \033[36mR$ {:.2F}\033[m '.format(BONUS))

