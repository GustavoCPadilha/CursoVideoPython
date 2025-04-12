"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
dados = []
maior_peso_lista = []
menor_peso_lista = []
maior_peso = 0
menor_peso = 0
contador = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    contador += 1
    continua = input('Quer continuar? [S/N] ').strip().lower() [0]
    if continua in 'sn':
        if continua == 'n':
            break
    else:
        while True:
           print('Opção inválida! Tente novamente.')
           continua = input('Quer continuar? [S/N] ').strip().lower()[0]
           if continua in 'sn':
                break

print('-='*30)
print(f'Ao todo, você cadastrou {contador} pessoas')

maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]
maior_peso_lista = [pessoas[0][0]]
menor_peso_lista = [pessoas[0][0]]

for p in pessoas[1:]:
    if p[1] > maior_peso:
        maior_peso = p[1]
        maior_peso_lista = [p[0]]
    elif p[1] == maior_peso:
        maior_peso_lista.append(p[0])

    if p[1] < menor_peso:
        menor_peso = p[1]
        menor_peso_lista = [p[0]]
    elif p[1] == menor_peso:
        menor_peso_lista.append(p[0])

print(f'O maior peso foi de {maior_peso}KG. Peso de {maior_peso_lista}')
print(f'O menor peso foi de {menor_peso}KG. Peso de {menor_peso_lista}')