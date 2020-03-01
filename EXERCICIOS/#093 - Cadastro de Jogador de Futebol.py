# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

print(f'Quantos gols {jogador["Nome"]} fez em cada partida ?')
for c in range(0, tot):
    partidas.append(int(input(f'    {c+1}º Partida: ')))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')

for i, v in enumerate(jogador['Gols']):
    print(f'    - {i+1}ª Partida: {v}')

print(f'    - Total = {jogador["Total"]} gols')