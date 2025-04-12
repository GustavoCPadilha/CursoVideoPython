"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla.
"""
from random import randint

valores = (
           randint(0,10),
           randint(0,10),
           randint(0,10),
           randint(0,10),
           randint(0,10)
          )
contador = maior = menor = 0

print(f'Os valores sorteados foram: ', end='')
for num in valores:
    if contador == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    contador += 1
    print(num, end=' ')

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')