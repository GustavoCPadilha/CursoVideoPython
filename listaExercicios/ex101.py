"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

from datetime import date

def voto(idade):
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade < 18 or idade >= 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

ano_atual = date.today().year
ano_nascimento = int(input("Em que ano você nasceu? "))
ano = ano_atual - ano_nascimento
print(voto(ano))
