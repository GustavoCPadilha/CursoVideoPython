"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))

if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 7 > aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print('-='*15)
for key, value in aluno.items():
    print(f'- {key} é igual a {value}')