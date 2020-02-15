N = str(input('Digite uma frase: ')).upper().strip()

print('Quantas vezes aparece a letra A? | R: {}'.format(N.count('A')))
print('Em qual posição ela aparece a primeira vez | R: {}'.format(N.find('A')+1))
print('Em qual posição ela aparece a ultima vez | R: {}'.format(N.rfind('A')+1))