#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
#https://youtu.be/664e0G_S9nU
#Adicionar cores

N = int(input('Digite um numero: '))

ANTE = N-1
SUCE = N+1

print('O seu antecessor é: \033[1;34;47m{}\033[m' .format(ANTE))
print('O seu sucessor é: \033[1;33;40m{}\033[m' .format(SUCE))