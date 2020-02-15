import math

N1 = int(input('Digite  o valor do cateto adjacente: '))
N2 = int(input('Digite o valor do cateto oposto: '))

print('O valor da Hypotenusa é {:.2f}'.format(math.hypot(N1,N2)))