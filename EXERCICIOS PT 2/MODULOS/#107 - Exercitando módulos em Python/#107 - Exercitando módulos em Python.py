from package import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {p} é {moeda.metade(p):.2f}')
print(f'O dobro de {p} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10):.2f}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13):.2f}')

