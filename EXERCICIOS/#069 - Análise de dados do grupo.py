# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
# https://youtu.be/4Ca6iRJo3M0

from time import sleep

cont_maior18 = cont_mulher_menor18 = cont_homens = 0

while True:
    print('=== INSIRA OS DADOS ===')
    idade = int(input('Digite a idade da primeira pessoa: '))
    sexo = str(input('Qual o sexo dessa pessoa: [M/F] ')).upper()

    if idade >= 18:
        cont_maior18 += 1
    if sexo in 'Mm':
        cont_homens += 1
    if sexo in 'Ff' and idade < 18:
        cont_mulher_menor18 += 1
    
    print('='*30)
    sequencia = str(input('Você deseja continuar? S/N'))
    print('='*30)

    if sequencia in 'Nn':
        break

print('='*30)
print('ANALISANDO...')
sleep(1)
print('---DOS DADOS DIGITADOS---')
sleep(1)
print(f'{cont_maior18} São maiores de idade')
sleep(1)
print(f'{cont_homens} São homens')
sleep(1)
print(f'{cont_mulher_menor18} São mulheres e menores de idade')

print('='*30)

print('FIM')