#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
#https://youtu.be/d2ug6quC1bk

n = soma = cont = 0

while True:

    soma += n
    

    n = int(input('Digite um número: '))
    
    if n == 999:
        break

    cont += 1

print(f'Você digitou {cont} numero e a soma entre eles foi {soma}')

