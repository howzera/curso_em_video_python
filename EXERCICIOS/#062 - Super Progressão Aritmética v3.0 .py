# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# https://youtu.be/BWAWq7n6PCk

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
prog = primeiro_termo

count = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total:
    
        print('{}...'.format(prog), end='►')
        prog += razão
        count += 1

    print('Pause')
    mais = int(input('Quantos termos você quer mostrar a mais?'))

print('FIM')