"""
Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.
"""

import moeda

preco = float(input("Digite um preço: R$"))

print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(preco, 10, True)}")
print(f"O dobro de {preco} é {moeda.metade(preco, True)}")
print(f"A metade de {preco} é {moeda.dobro(preco, True)}")