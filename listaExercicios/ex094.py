"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
pessoa = dict()
pessoas = list()
soma = 0

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: ').strip().lower()[0]
    while pessoa['sexo'] not in 'fm':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo: ').strip().lower()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    soma += pessoa['idade']
    while continua not in 'sn':
        print('ERRO! Responda apenas S ou N.')
        continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continua == 'n':
        break

media = soma / len(pessoas)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media}')
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'f':
        print(f'{p['nome']} ', end='')
print('\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        for key, value, in pessoa.items():
            print(f'{key} = {value};', end=' ')
print('\n<< ENCERRADO >>')