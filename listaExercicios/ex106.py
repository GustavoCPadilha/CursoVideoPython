"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""

print("SISTEMA DE AJUDA PyHELP")
while True:
    ajuda = input("Função ou Biblioteca: ")
    if ajuda.lower() == 'fim':
        break
    help(ajuda)
