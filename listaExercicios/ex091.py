"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador1' : randint(1,6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for key, value in jogadores.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)
print('-='*20)
print('== RANKING DOS JOGADORES ==')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}.')