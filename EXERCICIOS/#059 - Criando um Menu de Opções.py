#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
#https://youtu.be/OBJL5vPj4-E

n1 = int(input('Digite o primeiro valor: '))

n2 = int(input('Digite o segundo valor: '))

print('''==== O QUE DESEJA FAZER? ====
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR 
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA 
===============================''')

opção = -1

while opção != 5:
    opção = int(input('Digite a opção: '))

    if opção == 1:
        print('A soma dos numeros é: {}'.format(n1 + n2))
    elif opção == 2:
        print('A multiplicação dos numeros é: {}'.format(n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior numero é: {}'.format(n1))
        else:
            print('O maior numero é: {}'.format(n2))
    elif opção == 4:
        print('Digite novos números:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('PROGRAMA ENCERRADO!')
        break
    else:
        print('Opção inváloda, tente novamente')
