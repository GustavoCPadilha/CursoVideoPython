"""
Simulador de Caixa Eletrônico
"""

print('='*30)
print('      BANCO DO GUSTAVÃO')
print('='*30)

nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_1 = 0
valor = int(input('Qual valor você quer sacar? R$'))

while valor > 0:
    if valor >= 100:
        nota_100 += 1
        valor -= 100
    elif valor >= 50:
        nota_50 += 1
        valor -= 50
    elif valor >= 20:
        nota_20 += 1
        valor -= 20
    elif valor >= 10:
        nota_10 += 1
        valor -= 10
    elif valor  >= 5:
        nota_5 += 1
        valor -= 5
    else:
        nota_1 += 1
        valor -= 1

if nota_100 > 0:
    print(f'Total de {nota_100} cédulas de R$100')
if nota_50 > 0:
    print(f'Total de {nota_50} cédulas de R$50')
if nota_20 > 0:
    print(f'Total de {nota_20} cédulas de R$20')
if nota_10 > 0:
    print(f'Total de {nota_10} cédulas de R$10')
if nota_5 > 0:
    print(f'Total de {nota_5} cédulas de R$5')
if nota_1 > 0:
    print(f'Total de {nota_1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO DO GUSTAVÃO! Tenha um bom dia!')