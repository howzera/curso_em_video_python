# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# https://youtu.be/mw1So0r317Y

from datetime import datetime

dados = {}

dados['Nome'] = str(input('digite um nome: '))
idade = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - idade
dados['Carteira de Trabalho'] = int(input('Digite a carteira de trabalho: (0 se não tiver)'))

if dados['Carteira de Trabalho'] > 0:
    dados['Contrato'] = int(input('Digite o ano de contratação: '))
    dados['Salario'] = int(input('Digite o salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contrato'] + 35) - datetime.now().year)
print('-='*30)

for c, v in dados.items():
    print(f' - {c} tem o valor {v}')