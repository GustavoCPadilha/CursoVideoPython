"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""

from random import randint
from time import sleep

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
numeros = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {jogos} JOGOS', '-='*3)

for cada in range(0,jogos):
    for c in range(0, 6):
        num = randint(0,60)
        if num not in numeros:
            numeros.append(num)
        numeros.sort()
    print(f'Jogo {cada+1}: {numeros}')
    numeros.clear()
    sleep(1)

print('-='*5, '< BOA SORTE!>','-='*5)