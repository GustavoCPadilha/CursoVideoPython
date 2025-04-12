"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

print('-'*25)
print('   CADASTRE UMA PESSOA')
print('-'*25)

maioridade = 0
homem = 0
mulher_menor_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()[0]
    while sexo not in 'mf':
        print('Sexo inválido. Tente novamente')
        sexo = input('Sexo [M/F]: ').strip().lower()[0]

    if idade > 18:
        maioridade += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher_menor_20 += 1

    print('-' * 25)

    seguir = input('Quer continuar? [S/N] ').strip().lower() [0]

    if seguir == 'n':
        break

print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menor_20} mulheres com menos de 20 anos')