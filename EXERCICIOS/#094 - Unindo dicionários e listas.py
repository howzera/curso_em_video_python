# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
# https://youtu.be/mw1So0r317Y

dados = {}
lista = []
idade = []
lista_F = []
lista_ac_media = []

while True:

    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [M/F] '))
    dados['Idade'] = int(input('Idade: '))
    idade.append(dados['Idade'])


    while dados['Sexo'] not in 'MmFf':
        print('Dados inválidos, por favor insira novamente!!!')
        dados['Sexo'] = str(input(' [M/F] '))
    lista.append(dict(dados))

    if dados['Sexo'] in 'Ff':
        lista_F.append(dict(dados))
    
    opc = input('Quer continuar ? [S/N]')
    if opc not in 'SsNn':
        opc = input('OPÇÃO INVÁLIDA, DIGITE NOVAMENTE!')
    elif opc in 'Nn':
        break

print('-='*30)
print(f'{"ANALISE DE DADOS":-^30}')
print('-='*30)

print(f'{"-QUANTIDADE DE PESSOAS CADASTRADAS":<50}', end ='|: ')
print(len(lista))

print(f'{"-A MÉDIA DE IDADE FOI DE":<50}', end ='|: ')
media = sum(idade) / len(idade)
print(f'{idade:.1f}')

print(f'{"-AS MULHERES CADASTRADAS FORAM":<50}', end='|: \n')

for c in range(0, len(lista_F)):
    print(f' - {lista_F[c]["Nome"]}')

for c in range(0,len(lista)):
    if lista[c]['Idade'] > (sum(idade) / len(idade)):
        lista_ac_media.append(lista[c])

print(f'{"-AS PESSOAS COM IDADE ACIMA DA MÉDIA FORAM":<50}', end='|: \n')
for c in range(0, len(lista_ac_media)):
    print(f' - {lista_ac_media[c]["Nome"]} com idade de {lista_ac_media[c]["Idade"]}')

