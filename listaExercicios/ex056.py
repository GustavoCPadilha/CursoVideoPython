"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
idade_total = 0
homem_velho_idade = 0
homem_velho = ''
total_mulheres = 0

for c in range(1, 5):
    print(f'-----{c}° PESSOA-----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    if sexo == 'M':
        if homem_velho_idade < idade:
            homem_velho_idade = idade
            homem_velho = nome
    if sexo == 'F':
        if idade < 20:
            total_mulheres += 1
    idade_total += idade
print(f'A média de idade do grupo é de {idade_total/4}.')
print(f'O homem mais velho tem {homem_velho_idade} e se chama {homem_velho}.')
print(f'Ao todo são {total_mulheres} mulheres com menos de 20 anos.')