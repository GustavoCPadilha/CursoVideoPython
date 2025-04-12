"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.
"""

contador = 0
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = input('Quer continuar? [S/N] ').strip().lower() [0]
    contador += 1
    if continua in 'sn':
        if continua == 'n':
            break
    else:
        while True:
            print('Opção inválida! Tente novamente.')
            continua = input('Quer continuar? [S/N] ').strip().lower()[0]
            if continua in 'sn':
                break
        if continua == 'n':
            break
            
lista.sort(reverse=True)
print(f'Você digitou {contador} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
