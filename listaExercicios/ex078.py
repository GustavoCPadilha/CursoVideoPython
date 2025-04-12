"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
maior = menor = 0

for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {contador}: ')))
    if contador == 0:
        maior = menor = lista[0]
    elif lista[0+contador] > maior:
        maior = lista[0+contador]
    elif lista[0+contador] < menor:
        menor = lista[0+contador]

print('=-'*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice+1}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice+1}...', end='')