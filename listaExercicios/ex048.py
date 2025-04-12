"""
Faça um programa que calcule a soma entre todos os números que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

contador = 0
n = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        n = n + c
        contador = contador + 1
print(f'A soma de todos os {contador} valores solicitados é {n}')