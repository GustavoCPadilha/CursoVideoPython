"""
Progressão Aritmética v2.0 (Usando While)
"""

print('-='*10)
print('Gerador de PA')
print('-='*10)

num1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
while contador != 10:
    if contador == 0:
        print(f'{num1}', end=' ' '-> ')
        contador += 1
    num1 += razao
    print(f'{num1}', end=' ' '-> ')
    contador += 1
print('FIM')