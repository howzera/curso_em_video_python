N = str(input('Digite seu nome completo: ')).upper().strip()

nome = N.split()

print('Primeiro: {}'.format(nome[0]))
print('Ultimo: {}'.format(nome[len(nome)-1]))
