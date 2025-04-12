"""
Jogo da Adivinhação v.1.0
"""
from random import randint

num_computador = randint(0,5)
print('-' * 60)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 60)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if num == num_computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_computador} e não no {num}!')
