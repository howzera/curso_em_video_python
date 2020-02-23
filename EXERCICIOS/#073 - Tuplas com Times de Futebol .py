# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados 
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.


times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR','São Paulo',
        'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
        'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
        'Chapecoense', 'Avaí')



print('=== TABELA BRASILEIRÃO ===')
print('='*30)
print(f'Lista de Times: {times}')
print('='*30)

print('=== 5 PRIMEIROS COLOCADOS ===')
for c in range(len(times[:5])):
    print(f'{c+1}º Colocado - {times[c]}')

print('='*30)

print('=== OS 4 ULTIMOS COLOCADOS ===')


for c in range(15, len(times)):
    print(f'{c+1}º Colocado - {times[c]}')

print('='*30)

print('')

print('=== TIMES EM ORDEM ALFABÉTICA ===')

print(f'{sorted(times)}')

print('='*30)

print('')

print('=== POSIÇÃO CHAPECOENCE ===')

print(f'O Chapecoence está na posição {times.index("Chapecoense")+1}ª posição')