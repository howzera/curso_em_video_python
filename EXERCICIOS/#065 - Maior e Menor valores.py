#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
#https://youtu.be/QNPuPlPM--0

print('-='*30)

cont = media = soma = maior = menor = 0

continuar = 'S'

while continuar in 'Ss':

    n = int(input('Digite um número: '))

    soma += n
    cont += 1

    if cont == 1:
        maior = menor = n
    
    else:

        if n < menor:
            menor = n

        if n > maior:
            maior = n
        

    continuar = str(input('DESEJA CONTINUAR ? S/N: ')).upper().strip()[0]

media = soma / cont

print('-='*30)

print('Você digitou {} numeros e a média entre os valores digitados foi: {}'.format(cont, media))

print('O maior: {}'.format(maior))

print('O menor: {}'.format(menor))
