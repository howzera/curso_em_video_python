n = (int(input('Digite o 1º número: ')),
     int(input('Digite o 2º número: ')),
     int(input('Digite o 3º número: ')),
     int(input('Digite o 4º número: ')))


cont = 0

for c in n:
    if c == 9:
        cont += 1
print(f'O número 9 apareceu {cont} vezes')


print(f'Os números pares foram: ', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=', ')

print('...')

for p, c in enumerate(n):
    if c == 3:
        print(f'O dígito 3 foi encontrado na posição {p}')
        break