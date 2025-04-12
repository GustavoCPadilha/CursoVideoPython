"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é de {a}m².')


print('Controle de Terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)