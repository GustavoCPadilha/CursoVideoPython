"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

pessoas = dict()
pessoas['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
pessoas['idade'] = datetime.today().year - nasc
pessoas['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoas['ctps'] == 0:
    print('-='*20)
    for key, value in pessoas.items():
        print(f'- {key} tem o valor {value}')
else:
    pessoas['contratacao'] = int(input('Ano de Contratação: '))
    pessoas['salario'] = float(input('Salário: R$'))
    pessoas['aposentadoria'] = pessoas.get('idade') + 35  #Evitar o aviso do python kkk
    print('-=' * 20)
    for key, value in pessoas.items():
        print(f'- {key} tem o valor de {value}')