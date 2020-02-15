#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#https://youtu.be/_Nk02-mfB5I

from random import choice

N1 = input('Digite o nome do primeiro aluno: ')
N2 = input('Digite o nome do segundo aluno: ')
N3 = input('Digite o nome do terceiro aluno: ')
N4 = input('Digite o nome do quarto aluno: ')

LISTA = [N1, N2, N3, N4]

print('O aluno escolhido foi {}'.format(choice(LISTA)))

