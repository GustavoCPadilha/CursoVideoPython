"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
peso_maior = 0.0
peso_menor = 0.0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    if peso > peso_maior:
        peso_maior = peso
    if peso < peso_menor:
        peso_menor = peso
print(f'O maior peso lido foi de {peso_maior}Kg')
print(f'O menor peso lido foi de {peso_menor}Kg')