"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
from time import sleep

possiveis_jogadas_bot = ['PEDRA', 'PAPEL', 'TESOURA']
jogada_bot = random.choice(possiveis_jogadas_bot)
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
jogada_usuario = int(input('Qual é sua jogada? '))

if jogada_usuario == 0:
    jogada_usuario = 'PEDRA'
elif jogada_usuario == 1:
    jogada_usuario = 'PAPEL'
elif jogada_usuario == 2:
    jogada_usuario = 'TESOURA'
else:
    print('Jogada inválida. Tente novamente!')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 20)
print(f'Computador jogou {jogada_bot}')
print(f'Jogador jogou {jogada_usuario}')
print('-=' * 20)

if jogada_usuario == 'PEDRA' and jogada_bot == 'TESOURA':
    print('JOGADOR VENCE')
elif jogada_usuario == 'PAPEL' and jogada_bot == 'PEDRA':
    print('JOGADOR VENCE')
elif jogada_usuario == 'TESOURA' and jogada_bot == 'PAPEL':
    print('JOGADOR VENCE')
elif jogada_usuario == jogada_bot:
    print('EMPATE')
else:
    print('COMPUTADOR VENCE')
