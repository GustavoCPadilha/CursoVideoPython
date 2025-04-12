"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
pares = soma = cont = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if cont == 0:
                maior = matriz[l][c]
                cont = 1
            elif matriz[l][c] > maior:
                maior = matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*20)

print(f'A soma de todos os pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')