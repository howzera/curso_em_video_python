from random import shuffle

N1 = input('Digite o nome do primeiro aluno: ')
N2 = input('Digite o nome do segundo aluno: ')
N3 = input('Digite o nome do terceiro aluno: ')
N4 = input('Digite o nome do quarto aluno: ')

LISTA = [N1, N2, N3, N4]
shuffle(LISTA)

print('A ordem de apresentação será: ')
print(LISTA)