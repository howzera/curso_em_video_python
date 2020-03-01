# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.#
# https://youtu.be/HipQYUk4koA

dados = {}

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))

print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')

if dados['media'] >= 7:
    dados['situação'] = "APROVADO"
elif 5 < dados['media'] < 7:
    dados['situação'] = "RECUPERAÇÃO"
else:
    dados['situação'] = "REPROVADO"

for k, i in dados.items():
    print(f'- {k} é igual á {i}')

