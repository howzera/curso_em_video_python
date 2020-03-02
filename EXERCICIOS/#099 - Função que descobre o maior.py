# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
#https://youtu.be/vp9UX7wr92o

from time import sleep
from random import randint

def maior(*num):
    
    cont = maior = 0
    print('Analisando os valores passados... ')

    for valor in num:
        print(f'{valor} ', end = '', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))
maior(randint(1,9), randint(1,9), randint(1,9))
maior(randint(1,9), randint(1,9))
maior(randint(1,9))




