"""
Maior e menor valores
"""

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

if num1 < num2 and num1 < num3:
    print(f'O menor valor digitado foi {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor valor digitado foi {num2}')
else:
    print(f'O menor valor digitado foi {num3}')

if num1 > num2 and num1 > num3:
    print(f'O maior valor digitado foi {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior valor digitado foi {num2}')
else:
    print(f'O maior valor digitado foi {num3}')

