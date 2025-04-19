"""
Adapte o código do desafio #107, criando uma função adicional chamada
moeda() que consiga mostrar os números como um valor monetário formatado.
"""

from utilidadescev import moeda

preco = float(input("Digite um preço: R$"))

print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco))}")
print(f"Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
