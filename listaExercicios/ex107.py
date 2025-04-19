"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.
"""
from utilidadescev import moeda


preco = float(input("Digite um preço: R$"))

print(f"Aumentando 10%, temos R${moeda.aumentar(preco)}")
print(f"Diminuindo 10%, temos R${moeda.diminuir(preco)}")
print(f"O dobro de R${preco} é R${moeda.metade(preco)}")
print(f"A metade de R${preco} é {moeda.dobro(preco)}")
