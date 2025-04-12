"""
Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

times_brasileirao = (
    "Corinthians",
    "Palmeiras",
    "Santos",
    "Grêmio",
    "Cruzeiro",
    "Flamengo",
    "Vasco da Gama",
    "Chapecoense",
    "Atlético-MG",
    "Botafogo",
    "Athletico-PR",
    "Bahia",
    "São Paulo",
    "Fluminense",
    "Sport Recife",
    "EC Vitória",
    "Coritiba",
    "Avaí",
    "Ponte Preta",
    "Atlético-GO"
)
print('-='*20)
print(f'Lista de times do Brasileirão (2017): {times_brasileirao}')
print('-='*20)
print(f'Os 5 primeiros são {times_brasileirao[:5]}')
print('-='*20)
print(f'Os 4 últimos são {times_brasileirao[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print('-='*20)
print(f'A Chapecoense está na {times_brasileirao.index('Chapecoense')+1}° posição')