#Ler o salário de um funcionário e mostrar seu novo salário com 15% de aumento.
#https://youtu.be/cTkivN8XcJ0


N = float(input('Digite seu salário: R$ '))

BONUS = N*1.15

print('Seu novo salário é: R$ {:.2F} '.format(BONUS))

