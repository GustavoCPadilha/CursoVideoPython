"""
Procurando uma string dentro de outra
"""

nome = input('Qual é seu nome completo? ')
nome = nome.lower()
nome = nome.split()
if 'silva' in nome:
    print('Seu nome tem Silva?', True)
else:
    print('Seu nome tem Silva?', False)