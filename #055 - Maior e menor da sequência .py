#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
#https://youtu.be/Kjpb_IAOKRQ

peso_maior = 0
peso_menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print('O menor peso foi {} Kg'.format(peso_menor))
print('O maior peso foi {} Kg'.format(peso_maior))
