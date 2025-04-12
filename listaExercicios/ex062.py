"""
Super Progressão Aritmética v3.0
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

print('-='*10)
print('Gerador de PA')
print('-='*10)

num1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
termo = -1
while contador != 10:
    if contador == 0:
        print(f'{num1}', end=' ' '-> ')
        contador += 1
    num1 += razao
    print(f'{num1}', end=' ' '-> ')
    contador += 1
print('PAUSA')
contador = 0
termo = int(input('Quantos termos você quer mostrar a mais? '))
while termo != 0:
    if termo == 0:
        break
    else:
        while contador != termo:
            num1 += razao
            print(f'{num1}', end=' ' '-> ')
            contador += 1
        contador = 0
        print('PAUSA')
        termo = int(input('Quantos termos você quer mostrar a mais? '))
