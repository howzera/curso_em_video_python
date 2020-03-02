# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões 
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# https://youtu.be/oV1s53YGtvE


print(f'{"PARÂMETROS TERRENOS":^30}')
print('-'*30)

def area(larg, comp):
    a = larg * comp
    print(f'A ÁREA DO TERRENO É DE {larg} x {comp}: {a:.1f} M²')


area(float(input('LARGURA: ')),
     float(input('COMPRIMENTO:  '))
    )
