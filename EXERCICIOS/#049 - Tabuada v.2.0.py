#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#https://youtu.be/QtElJDa9ICM

n = int(input('Digite um numero: '))

print('\033[1;31m-=\033[m'*7)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))

print('\033[1;31m-=\033[m'*7)