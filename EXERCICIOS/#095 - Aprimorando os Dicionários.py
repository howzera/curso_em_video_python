# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# https://youtu.be/mw1So0r317Y

dados = {}
gols = []
jogadores = []


while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou ? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos GOLS {dados["Nome"]} fez na partida {c+1} ? '))) 
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    gols.clear()
    jogadores.append(dados.copy())

    opc = str(input('Quer continuar ?')).upper()[0]
    if opc in 'N':
        break

print(f'{"ANALISE DE JOGADOR":-^60}')
print(' cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 PARA PARAR)'))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com esse código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}:')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*60)

print(f'{"ANALISE CONCLUÍDA":-^60}')
