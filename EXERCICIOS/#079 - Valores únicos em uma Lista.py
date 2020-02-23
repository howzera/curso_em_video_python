# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
# https://youtu.be/LkAzRnc_GPk

valores = []
op = 'S'

while op in 'Ss':

    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado!Não vou adicionar...')
        
    op = (str(input('Deseja continuar: [S/N] ').upper()))

    
print('==VALORES DIGITADOS==')

valores.sort()

print(f'{valores}', end = '...')
