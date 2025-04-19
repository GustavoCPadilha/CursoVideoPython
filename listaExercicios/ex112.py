"""
Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função imputa(), mas com uma
validação de dados para aceitar apenas valores que seja monetários.
"""
from utilidadescev import moeda
from utilidadescev import dado


preco = dado.leia_dinheiro("Digite um preço: R$")
moeda.resumo(preco, 20, 12)