# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
# https://youtu.be/uk0gDFQEo_I

lista = []
par = []
impar = []

while True:
    
    n = int(input('Digite um valor: '))
    lista.append(n)

    opc = str(input('Deseja continuar? [S/N]')).upper()

    while opc not in 'NnSs':
        
        op = input('Opção inválida!!! Digite novamente: [S/N]').upper()
        
    if op in 'Nn':
        break

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('='*30)
print(f'{"LISTA":=^30}')
print(lista)
print('-='*30)
print(f'{"NÚMEROS PARES":=^30}')
par.sort()
print(par)
print('-='*30)
print(f'{"NÚMEROS ÍMPARES":=^30}')
impar.sort()
print(impar)
print('='*30)
print(f'{"FIM":=^30}')

    




