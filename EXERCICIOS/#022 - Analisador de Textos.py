#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
#https://youtu.be/EQQt-6QqXOs

nome = str(input('Digite seu nome completo: '))

print('Fazendo analise do nome.....')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()
print('Seu primeiro nome "{}" tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))