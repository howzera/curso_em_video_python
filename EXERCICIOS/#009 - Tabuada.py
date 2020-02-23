#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
#https://www.youtube.com/watch?v=qajq3SI0QQs
#Adicionar cores

N = int(input('Digite um numero inteiro: '))

print('\nTÁBUADA DE {}'.format(N))

print('\033[1;36m='*15)

print('\033[1;37m{}\033[m X 1 = \033[1;37m{}\033[m'.format(N, N*1))
print('\033[1;36m{}\033[m X 2 = \033[1;36m{}\033[m'.format(N, N*2))
print('\033[1;35m{}\033[m X 3 = \033[1;35m{}\033[m'.format(N, N*3))
print('\033[1;34m{}\033[m X 4 = \033[1;34m{}\033[m'.format(N, N*4))
print('\033[1;33m{}\033[m X 5 = \033[1;33m{}\033[m'.format(N, N*5))
print('\033[1;32m{}\033[m X 6 = \033[1;32m{}\033[m'.format(N, N*6))
print('\033[1;31m{}\033[m X 7 = \033[1;31m{}\033[m'.format(N, N*7))
print('\033[1;30m{}\033[m X 8 = \033[1;30m{}\033[m'.format(N, N*8))
print('\033[1;37m{}\033[m X 9 = \033[1;37m{}\033[m'.format(N, N*9))
print('\033[1;36m{}\033[m X 10 =\033[1;36m{}\033[m'.format(N, N*10))


print('\033[1;36m='*15)