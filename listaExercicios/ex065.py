"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

parar = True
cont = soma = maior = menor = 0
while parar:
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    continua = input('Quer continuar? [S/N]: ').upper()
    cont += 1
    soma += n
    if continua == 'N':
        parar = False
print(f'Você digitou {cont} números e a média foi {soma/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')