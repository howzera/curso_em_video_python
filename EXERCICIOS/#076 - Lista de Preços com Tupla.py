# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de 
# produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# https://youtu.be/Qp2cXfCHk2I


lista = ('Whey Baunilha', 75.00,
         'Whey Chocolate', 75.00,
         'Whey Morango', 75.00,
         'Hyper Mass 5KG', 105.00,
         'Creatina 300g', 70.00)


print('='*40)
print(f'{"Listagem De Produtos":=^40}')
print('='*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')

print('='*40)
print(f'{"FIM DA LISTA":=^40}')
print('='*40)

