#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#https://youtu.be/cyGY_83m4Xw

N = int(input('Digite o ano: '))

if (N % 4) == 0:
    if N % 100 > 0:
     print('O Ano {} é bissexto'.format(N))
elif (N % 400) == 0:
    print('O Ano {} é bissexto'.format(N))
else:
    print('O ano {} não é bissexto'.format(N))
