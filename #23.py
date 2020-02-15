N = int(input('Digite um numero entre 1 e 9990: '))

u = N // 1 % 10
d = N // 10 % 10
c = N // 100 % 10
m = N // 1000 % 10



print('O numero contém {} unidades' .format(u))
print('O numero contém {} dezenas' .format(d))
print('O numero contém {} centenas' .format(c))
print('O numero contém {} Milhar' .format(m))