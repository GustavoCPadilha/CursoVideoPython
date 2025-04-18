"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""
boletim = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continua = input('Quer continuar? [S/N] ').strip().lower()[0]

    while continua not in 'sn':
        print('Opção inválida! Tente novamente.')
        continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continua == 'n':
        break

print('-='*30)
print(f'No. NOME {'MÉDIA':^25}')
print('-'*30)

for i, aluno in enumerate(boletim):
    print(f'{i:<3} {aluno[0]:<15} {aluno[2]:>4.1f}')

while True:
    historico = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if historico == 999:
        break
    if 0 <= historico < len(boletim):
        print(f'Notas de {boletim[historico][0]} são {boletim[historico][1]}')
    else:
        print('Aluno não encontrado! Tente novamente.')

