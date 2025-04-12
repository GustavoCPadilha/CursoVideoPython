"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input('Digite um número: '))
contador = 0

for c in range(1 ,num+1):
    print(c, end=' ')
    if num % c == 0:
        contador +=  1
print(f'\nO número {num} foi divisível {contador} vezes')
if contador > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')

