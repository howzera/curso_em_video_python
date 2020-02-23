#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
#https://youtu.be/vu5ehetQGe8


primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
prog = primeiro_termo

count = 1

while count <= 10:
    
    print('{}...'.format(prog), end='►')
    prog += razão
    count += 1

print('Foram exibidos {} termos'.format(count))