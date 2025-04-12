"""
Jogo do Par ou Ímpar
"""

from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

venceu = True
qtde_vitorias = 0

while venceu:
    n_bot = randint(0, 10)
    n = int(input('Diga um valor: '))
    par_impar = input('Par ou Ímpar? [P/I]: ').lower()
    soma = n_bot + n
    print('-'*30)
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {n_bot}. Total de {soma} DEU PAR')
    else:
        print(f'Você jogou {n} e o computador {n_bot}. Total de {soma} DEU ÍMPAR')
    print('-'*30)

    if par_impar == 'p' and soma % 2 == 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        qtde_vitorias += 1
    elif par_impar == 'i' and soma % 2 == 1:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        qtde_vitorias += 1
    else:
        print('VOCÊ PERDEU!')
        venceu = False

print(f'GAME OVER! Você venceu {qtde_vitorias} vezes.')