"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogadores = dict()
gol_partida = list()
lista = list()

while True:
    jogadores['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    gol_partida.clear()
    for i in range(partidas):
        gol_partida.append(int(input(f'    Quantos gols na partida {i+1}? ')))
    jogadores['gols'] = gol_partida.copy()
    jogadores['total'] = sum(gol_partida)
    lista.append(jogadores.copy())
    while True:
        continua = input('Quer continuar? [S/N] ').strip().lower()
        if continua in 'sn':
            break
        print('ERRO! Digite apenas S ou N')
    if continua == 'n':
        break

print('-=' * 30)
print(f'{"cod":<4} {"nome":<15} {"gols":<20} {"total":<5}')
print('-' * 50)
for indice, jogador in enumerate(lista):
    print(f'{indice:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<20} {jogador["total"]:<5}')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        break
    if 0 <= busca < len(lista):
        print(f' --- LEVANTAMENTO DO JOGADOR {lista[busca]['nome']}:')
        for i, gol in enumerate(lista[busca]['gols']):
            print(f'No jogo {i+1} fez {gol} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {busca}.')
print('<< VOLTE SEMPRE >>')