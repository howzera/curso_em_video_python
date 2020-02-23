#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#https://youtu.be/w7yn1_Mfu0E


print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos quer mostrar ?\n'))

t1 = 0
t2 = 1

print('~'*30)

print('{} ► {}'.format(t1, t2), end='')

cont = 3

while cont <= n:
    t3 = t1 + t2

    print('► {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('')
print('~'*30)
print('\n --- FIM --- ')

