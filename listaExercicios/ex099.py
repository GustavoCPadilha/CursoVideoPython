"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*args):
    maior_valor = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in args:
        print(f"{valor}", end=' ')
        if maior_valor < valor:
            maior_valor = valor
    print(f"Foram informados {len(args)} valores ao todo.")
    print(f"O maior valor informado foi {maior_valor}")

maior(1, 6, 3, 4)
