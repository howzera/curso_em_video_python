#Calcular a quantidade de tinta necessária para pintar o m² de parede.
#https://youtu.be/mzSJpn9ldt4

L = float(input('Digite a largura: '))
A = float(input('Digite a altura: '))

AREA = L*A

TINTA = AREA/2

print('Será necessário {:.2f} Litros de tinta para pintar a parede com {} M²'.format(TINTA, AREA))