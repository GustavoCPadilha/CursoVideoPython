"""
Progressão Aritmética
"""

print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)
inicio = int(input('Primeiro termo: '))
passo = int(input('Razão: '))
decimo = inicio + (10 - 1) * passo

for c in range(inicio, decimo + passo, passo):
    print(c, '->', end=' ')
print('ACABOU', end=' ')