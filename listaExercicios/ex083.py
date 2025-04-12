"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
"""

exp = input('Digite a expressão: ')
pilha = []

for char in exp:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if pilha:
            pilha.pop()
        else:
            print('Sua expressão está errada!')
            break
else:
    if not pilha:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está errada!')