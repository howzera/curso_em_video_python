# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 


print('='*30)
print('========== LOJA ==========')
print('='*30)

nome = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preço do produto: '))

total = preco
mais_barato = preco
mais_barato_nome = nome
cont_maior_q1000 = 0

print('='*30)

while True:
    
    sequencia = str(input('Você quer continuar ? [S/N]')).upper().strip()[0]

    if sequencia in 'Nn':
        break
    
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    total += preco

    if preco  < mais_barato:
        mais_barato_nome = nome

    if preco > 1000:
        cont_maior_q1000 += 1
  
print('=== DADOS DA COMPRA ===')

print('')

print(f'- Valor total: R$ {total:.2f}')
print('')
print(f'- Produtos mais caro que R$ 1000.00: {cont_maior_q1000}')
print('')
print(f'- O produto mais barato é: {mais_barato_nome}')

print('')
print('='*30)