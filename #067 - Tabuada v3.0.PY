#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 
#

n = 0

while True:

    n = int(input('Digite um valor: '))

    if n < 0:
        break
    
    print(f'===TABUADA DE {n}==')

    print(f'\033[1;37m{n}\033[m X 1 = \033[1;37m{n*1}\033[m')
    print(f'\033[1;36m{n}\033[m X 2 = \033[1;36m{n*2}\033[m')
    print(f'\033[1;35m{n}\033[m X 3 = \033[1;35m{n*3}\033[m')
    print(f'\033[1;34m{n}\033[m X 4 = \033[1;34m{n*4}\033[m')
    print(f'\033[1;33m{n}\033[m X 5 = \033[1;33m{n*5}\033[m')
    print(f'\033[1;32m{n}\033[m X 6 = \033[1;32m{n*6}\033[m')
    print(f'\033[1;31m{n}\033[m X 7 = \033[1;31m{n*7}\033[m')
    print(f'\033[1;30m{n}\033[m X 8 = \033[1;30m{n*8}\033[m')
    print(f'\033[1;37m{n}\033[m X 9 = \033[1;37m{n*9}\033[m')
    print(f'\033[1;36m{n}\033[m X 10 =\033[1;36m{n*10}\033[m')

    print('='*30)
