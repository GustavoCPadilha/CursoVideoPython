"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [ [0,0,0], [0,0,0], [0,0,0] ]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l+1}, {c+1}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()