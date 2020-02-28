# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
#https://youtu.be/zPtvuLiEdKk]

lista = []
dados = []
maior = 0
menor = 0

while True:

    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite o peso dessa pessoa: ')))

    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()
 
    print('-'*30)
    
    opc = (input('Quer continuar ? [S/N]'))

    if opc in 'Nn':
        break



print(f'Foram cadastradas {len(lista)} pessoas.\n')
print(f'O maior peso cadastrado foi {maior} Kg entre os nomes:', end =' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}\n')
print(f'\nO menor peso cadastrado foi {menor} Kg entre os nomes:', end = ' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}\n')

