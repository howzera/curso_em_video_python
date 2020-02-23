#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#https://youtu.be/5VBWe6BXzRo

frase = str(input('Digite uma frase: ')).upper()
frase = frase.split()
junto = ''.join(frase)
inverso = junto[::-1]
print(inverso)

if junto == inverso:
    print('A palavra é um PALÍNDROMO')
else:
    print('A palavra NÃO É UM PALÍNDROMO')
