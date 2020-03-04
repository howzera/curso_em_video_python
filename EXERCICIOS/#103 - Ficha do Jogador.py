# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
# https://youtu.be/FbOvilKfHMI

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols}')

n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
    