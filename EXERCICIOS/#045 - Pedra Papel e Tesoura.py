#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
#https://youtu.be/tapTa6KVG-A

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')   

computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')


jogador = int(input('Qual é a sua jogada? \n'))

if jogador > 2:
    print('OPÇÃO INVÁLIDA')
else: 
    
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-='*11)
    print('O computador escolheu {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)

if computador == 0:

    if jogador == 0:
        print('O jogo empatou')
    elif jogador == 1:
        print('Você venceu')
    elif jogador == 2:
        print('Você perdeu')

elif computador == 1:

    if jogador == 0:
        print('Você perdeu')
    elif jogador == 1:
        print('O jogo empatou')
    elif jogador == 2:
        print('Você venceu')  

elif computador == 2:

    if jogador == 0:
        print('Você venceu')
    elif jogador == 1:
        print('Você perdeu')
    elif jogador == 2:
        print('Você empatou')
