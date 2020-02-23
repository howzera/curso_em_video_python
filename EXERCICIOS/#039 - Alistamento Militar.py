#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#https://youtu.be/ePwP4gU_waY

from datetime import date

n = int(input('Digite o seu ano de nascimento: '))

ano_atual = date.today().year

if (ano_atual - n) < 18:
    print('Você ainda não completou 18 anos e não precisa se alistar')
    print('Ainda falta {} anos para você se alistar'.format(abs((ano_atual-n)-18)))
elif (ano_atual - n) == 18:
    print('Você completou 18 anos e deve se alistar')
else:
    print('Você tem mais de 18, e se ainda não se alistou, apresentese ao exercito da sua cidade para regularizar sua posição  militar')
    print('Já se passaram {} anos para você se alistar'.format(abs((ano_atual-n)-18)))