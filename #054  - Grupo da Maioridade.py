#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#https://youtu.be/IL5iBWoKRIs

from datetime import date

ano_atual = date.today().year

menor_de_idade = 0

maior_de_idade = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - nasc < 18:
        menor_de_idade += 1
    elif ano_atual - nasc >= 18:
        maior_de_idade += 1

print('{} Dessas pessoas já são maiores de idade, e {} ainda são de menor'.format(maior_de_idade, menor_de_idade))
