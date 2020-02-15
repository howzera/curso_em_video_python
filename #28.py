from random import randint

n = randint(0, 5)

s = int(input('Digite um numero: '))

if s == n:
    print('Parabéns, você acertou o numero')
else:
    print('Infelizmente você errou')
