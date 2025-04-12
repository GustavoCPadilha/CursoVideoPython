"""
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0
cont = 0
for c in range(0,6):
    num = int(input('Digite algum número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma é de {soma}')