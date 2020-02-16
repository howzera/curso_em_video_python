#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
#https://youtu.be/ZiC5NgSGJXU

from datetime import date

n = int(input('Digite o ano de nascimento: '))

idade = abs(date.today().year - n)

if idade <= 9:
    print('ATLETA MIRIM')
elif idade > 9 and idade <= 14:
    print('ATLETA INFANTIL')
elif idade > 14 and idade <= 19:
    print('ATLETA JUNIOR')
elif idade > 19 and idade <= 20:
    print('ATLETA SENIOR')
else:
    print('ATLETA SENIOR')