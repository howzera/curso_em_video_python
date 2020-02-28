# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
#https://youtu.be/Hd7Ycaj61xE


from random import randint
from time import sleep

print('='*30)
print(f'\n{"JOGO DA MEGA SENA":^30}\n')
print('='*30)

lista = []
jogo = []
rodada = 1

print('')
print('-'*30)
partidas = int(input('Quantos jogos você quer que eu sorteie: '))
print('-'*30)

print('='*30)


while rodada <= partidas:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    rodada += 1

    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
