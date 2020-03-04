# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o 
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL 
# e OBRIGATÓRIO nas eleições.
# https://youtu.be/czDcimdc3GU

from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano

    if idade < 16:
        print(f'Você tem {idade} anos, com essa idade o voto é: PROÍBIDO!!!')
    elif idade >= 16 and idade < 18 or idade > 69:
        print(f'Você tem {idade} anos, com essa idade o voto é: OPICIONAL!!!')
    elif idade >= 18:
        print(f'Você tem {idade} anos, com essa idade o voto é: OBRIGATÓRIO!!!')

print('-'*15)
voto(int(input(f'Em que ano você nasceu? ')))