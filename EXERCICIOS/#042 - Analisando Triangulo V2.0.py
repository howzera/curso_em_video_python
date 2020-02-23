#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
#https://youtu.be/ZX7sCPjcHA0

a = float(input(('Digite o valor de A: ')))
b = float(input(('Digite o valor de B: ')))
c = float(input(('Digite o valor de C: ')))

if a < b+c and b < a+c and c < b+a:
    print('Este conjunto pode formar um \033[1;32mTriangulo \033[m')
    if a == b == c:
        print('Equilatero')
    elif a != b != c !=a:
        print('Escaleno')
    else:
        print('Isósceles')

else:
    print('Este conjunto não pode formar um \033[1;31mTriangulo \033[m')