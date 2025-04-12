"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continua in 'sn':
        if continua == 'n':
            break
    else:
        while True:
            print('Opção inválida! Tente novamente.')
            continua = input('Quer continuar? [S/N] ').strip().lower()[0]
            if continua in 'sn':
                break
        if continua == 'n':
            break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')