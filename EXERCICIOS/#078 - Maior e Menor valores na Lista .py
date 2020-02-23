# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
# https://youtu.be/q8Z1cRdJnfk

valores = []
maior = 0
menor = 0

for p, c in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor para a posição {c}: > ')))

    if c == 0:
        maior = menor = valores[c]
        posicaomaior = p
        posicaomenor = p
    
    else:
        if valores[c] > maior:
            maior = valores[c]
            posicaomaior = p
        elif valores[c] < menor:
            menor = valores[c]
            posicaomenor = p

print(f'O maior valor é: {maior} E foi encontrado na posição: {posicaomaior}')
print(f'O menor valor é :{menor} E foi encontrado na posição: {posicaomenor}')
