"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

ano_atual = date.today().year
menor_idade = 0
maior_idade = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if ano_atual - nasc >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade')
print(f'E também tivemos {menor_idade} pessoas menores de idade')