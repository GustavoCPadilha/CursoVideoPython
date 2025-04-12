"""
Custo da Viagem
"""

distancia = float(input("Qual é a distância da sua viagem? "))
print(f'Você está prestes a começar uma viagem de {distancia}.0Km.')
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f'E o preço da sua passagem será de R${passagem}')