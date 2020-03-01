# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# https://youtu.be/cwrqIztaAwk

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint(1, 6), 
        'jogador2' : randint(1, 6), 
        'jogador3' : randint(1, 6), 
        'jogador4' : randint(1, 6)}

count = 1

print(f'{"JOGADAS":=^30}')

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print(f'{"RANKING":=^30}')

for item in sorted(jogo, key = jogo.get):
    print(f'O {item} ficou em {count}º e jogou {jogo[item]} no dado')
    count+=1
    sleep(1)