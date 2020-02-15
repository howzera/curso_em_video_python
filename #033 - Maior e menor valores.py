#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#https://youtu.be/a_8FbW5oH6I

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a != b and b != c:
    if a > b and a > c:
        print('O maior numero é o atribuído ao A: {}'.format(a))
    elif b > a  and b > c:
        print('O maior numero é o atribuído ao B: {}'.format(b))
    elif c > a and c > b:
        print('O maior numero é o atribuído ao C: {}'.format(c))

    if a < b and a < c:
        print('O menor numero é o atribuído a letra A: {}'.format(a))
    elif b < a and b < c:
        print('O menor numero é o atribuído a letra B: {}'.format(b))
    elif c < a and c < b:
        print('O menor numero é o atribuído a letra C: {}'.format(c))
else:
    print('Os numero não podem ser iguais')
