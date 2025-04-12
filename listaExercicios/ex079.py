"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

valores = []

while True:
    num = int(input("Digite um valor: "))
    if num in valores:
        print("Valor duplicado! Não vou adicionar...")
    else:
        valores.append(num)
        print("Valor adicionado com sucesso...")
    continua = input('Quer continuar? [S/N] ').strip().lower() [0]
    if continua not in 'ns':
        print('Operação inválida! Tente novamente.')
        continua = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continua == 'n':
        break
        
valores.sort()
print(f'Você digitou os valores {valores}')
