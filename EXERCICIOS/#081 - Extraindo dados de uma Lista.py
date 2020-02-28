# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# https://youtu.be/SXJKAVVlvGAs

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    op = input('Quer continuar: [S/N]').upper()

    while op not in 'NnSs':
        
        op = input('Opção inválida!!! Digite novamente: [S/N]').upper()
        
    if op in 'Nn':
        break

print('-='*30)

print(f'{"LISTA":=^30}')

print(f'Foram digitados \033[1;32m{len(lista)}\033[m valores.')
    
print(f'{"ORDEM DECRESCENTE":=^30}')

lista.sort(reverse=True)

print(f'{lista}')

print(f'{"TEMOS O VALOR 5 ?":=^30}')

if 5 in lista:
    print('\033[1;32mO valor 5 está na lista!\033[m')
else:
    print('\033[1;31mNão encontramos o valor 5\033[m')