N = int(input('Digite o ano: '))

if (N % 4) == 0:
    if N % 100 > 0:
     print('O Ano {} é bissexto'.format(N))
elif (N % 400) == 0:
    print('O Ano {} é bissexto'.format(N))
else:
    print('O ano {} não é bissexto'.format(N))
