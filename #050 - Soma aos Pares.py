#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
#https://youtu.be/rJaBLOW57Jg

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += cont

print('A soma dos {} pares valores solicitados é {}'.format(cont, soma))
