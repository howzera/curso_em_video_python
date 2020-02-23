# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


n = ('Bicicleta', 'Raul', 'Fabin', 'Gameplay', 'Escada', 'Shopping', 'Sidoka', 'Atila', 'Gordin', 'Cocao', 'Markin', 'Vinicin', 'ViniMaromba','Arapatoda')

for c in n:

    print(f'\nNa palavra {c} suas vogais são: ', end='')

    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')