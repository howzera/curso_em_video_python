# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
# https://youtu.be/1u7oA8ckjAc


count = 0

n =( int(input('Digite 1º Número: ')),
     int(input('Digite 2º Número: ')),
     int(input('Digite 3º Número: ')),
     int(input('Digite 4º Número: ')))

print(f'Valores: {n}\n\n')
print('-='*30)
print('\n=== Quantas vezes o valor 9 apareceu? ===\n')
print(f'Apareceu {n.count(9)} vezes\n')
print('=== Em que posição foi digitado o primeiro valor 3 ===\n')

if int(3) in n:
    print(f'Apareceu primeiro na posição {n.index(3)+1}\n')
else:
    print(f'Não foi digitado nenhum valor 3\n')


print('=== Quais foram os números pares  ===\n')

for c in range(len(n)):

    if n[c] % 2 == 0:
        print(f'{n[c]}', end=' ')

 



