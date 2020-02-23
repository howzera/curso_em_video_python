#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#https://youtu.be/QroT8cZMRnc

N = str(input('Em que cidade você nasceu?')).strip()
print(N[:5].upper() == 'SANTO')