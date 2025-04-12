"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""
from random import randint

num_bot = randint(0, 10)
tentativas = 0
palpite = -1

print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
while num_bot != palpite:
    palpite = int(input('Qual é seu palpite? '))
    if num_bot > palpite:
        print('Mais... Tente mais uma vez.')
        tentativas += 1
    elif num_bot < palpite:
        print('Menos... Tente mais uma vez.')
        tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')