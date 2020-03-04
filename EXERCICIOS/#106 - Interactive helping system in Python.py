# Python exercise 106: Make a mini-system that utilizes Python Interactive Help. The user is going to type the
# command and the manual will show up. When the user types the word 'FIM' ('END'), the program will close. Important: Use colors.
# https://youtu.be/BMKYnZoxy88


from random import randint

c = ('\033[m',                    #0 - sem cores
     '\033[0;30;41m',             #1 - vermelho
     '\033[0;30;42m',             #2 - verde
     '\033[0;30;43m',             #3 - amarelo
     '\033[0;30;44m',             #4 - azul
     '\033[0;30;45m',             #5 - roxo
     '\033[7;30m',                #6 - branco
    )




def ajuda(com):
    print(c[randint(1,6)])
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)
    print(c[6])


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[6], end='')



#MAIN

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('ATÉ LOGO!')

