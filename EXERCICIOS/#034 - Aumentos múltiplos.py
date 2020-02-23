#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
#https://youtu.be/Sfadj_AzKHw

N = float(input('Digite seu salário atual: '))


if N > 1250:
    print('Seu novo salário é: {:.2f}'.format(N*1.10))
else:
    print('Seu novo salário é: {:.2f}'.format(N*1.15))
