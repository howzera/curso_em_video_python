# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
#https://youtu.be/7xrCJnniqMw

dados = []
lista = []

while True:    
    nome = str(input('NOME: '))
    notaA = float(input('NOTA A: '))
    notaB = float(input('NOTA B: '))
    media = (notaA + notaB) / 2
    dados.append([nome, [notaA, notaB], media])

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-'*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for c, p in enumerate(dados):
    print(f'{c:<4}{p[0]:<10}{p[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('DIGITE O CÓDIGO DO ALUNO PARA VER SEU BOLETIM: '))
    if opc <= len(dados) -1:
        print(f'BOLETIN DO ALUNO(a): {dados[opc][0]}\nNOTAS: {dados[opc][1]}')
    else:
        print('--- VOLTE SEMPRE ---')
