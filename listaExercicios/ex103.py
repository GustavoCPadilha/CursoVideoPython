"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de
mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nome = '<desconhecido>', gols = 0):
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

nom = input("Nome do jogador: ")
gol = input("Número de gols: ")

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nom == '':
    nom = '<desconhecido>'

print(ficha(nom, gol))