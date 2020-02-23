# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
# vai informar quantas cédulas de cada valor serão entregues.
# CÉDULAS 50, 20, 10, 1.

print('='*30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('='*30)

n = int(input('QUAL VALOR DESEJA SACAR ? R$ '))

total = n

ced = 50

total_ced = 0 
while True:
    
    if total >= ced:
        total -= ced
        total_ced+=1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cedulas de R$ {ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

