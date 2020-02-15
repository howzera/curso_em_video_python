nome = str(input('Digite seu nome completo: '))

print('Fazendo analise do nome.....')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()
print('Seu primeiro nome "{}" tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))