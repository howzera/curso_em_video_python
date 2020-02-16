#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
#https://youtu.be/iuPbB9uHczM

n1 = int(input('Digite um valor A: '))
n2 = int(input('Digite um valor B: '))

if n1 > n2:
    print('O valor \033[1;36mA = {}\033[m é maior que o valor \033[1;31mB = {}\033[m'.format(n1, n2))
elif n2 > n1:
    print('O valor \033[1;36mB = {}\033[m é maior que o valor \033[1;31mA = {}\033[m'.format(n2, n1))
else:
    print('Os valores \033[1;32mA = {}\033[m e \033[1;31mB = {}\033[m \033[1;34mSÃO IGUAIS\033[m'.format(n1, n2))