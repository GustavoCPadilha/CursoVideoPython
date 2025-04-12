"""
Crie um programa que leia o nome e o preço de vários produtos.
  programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print('-'*35)
print('         LOJA DO GUSTAVÃO')
print('-'*35)

total = 0.0
produto_1k = 0
mais_barato = ''
preco_barato = 0.0
contador = 0

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    total += preco

    if contador == 0:
        mais_barato = produto
        preco_barato = preco

    elif preco_barato > preco:
        preco_barato = preco
        mais_barato = produto

    contador += 1

    if preco > 1000:
        produto_1k += 1
    if continua == 'n':
        break

print(f'O total da compra foi R${total}')
print(f'Temos {produto_1k} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {mais_barato} que custa {preco_barato}')