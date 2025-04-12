"""
Cálculo do Fatorial
"""


num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)