"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

jogadores = dict()
gol_partida = list()

jogadores['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogadores['nome']} jogou? '))
for i in range(0, partidas):
    gol_partida.append(int(input(f'    Quantos gols na partida {i+1}? ')))
jogadores['gols'] = gol_partida.copy()
jogadores['total'] = 0
for n in gol_partida:
    jogadores['total'] += n
print('-='*30)
print(jogadores)
print('-='*30)

for key, value in jogadores.items():
    print(f'O campo {key} tem o valor {value}')
print('-='*30)
print(f'O jogador {jogadores['nome']} jogou {partidas} partidas.')

for indice in range(0, partidas):
    print(f'    => Na partida {indice+1}, fez {gol_partida[indice]} gols.')
print(f'Foi um total de {jogadores['total']} gols.')