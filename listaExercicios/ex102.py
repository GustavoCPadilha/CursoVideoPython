"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num = 1, show = True):
    f = 1
    for i in range (num, 0, -1):
        f *= i
        if show:
            if i == 1:
                print(f"{i} =", end=' ')
            else:
                print(f"{i} x", end=' ')
    return f


n = int(input("Digite um número para ver seu fatorial: "))
conta = input("Quer ver a conta? [S/N] ").strip().lower()[0]
if conta == 's':
    conta = True
else:
    conta = False
print(fatorial(n, conta))