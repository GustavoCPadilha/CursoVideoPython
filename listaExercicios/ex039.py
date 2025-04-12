"""
Alistamento Militar
"""
from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
ano_alist = ano_atual - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {ano_alist} anos em {ano_atual}')

if ano_alist == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif ano_alist < 18:
    print(f'Ainda faltam {18 - ano_alist} anos para o alistamento')
else:
    print(f'Você já deveria ter se alistado há {ano_alist - 18} anos')