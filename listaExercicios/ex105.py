"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""

def notas(*notas, mostra_situacao = False):
    resposta = dict()
    maior = menor = cont = soma = 0
    for nota in notas:
        if cont == 0:
            maior = nota
            menor = nota
        if maior < nota:
            maior = nota
        if menor > nota:
            menor = nota
        cont += 1
        soma += nota
    resposta["total"] = cont
    resposta["maior"] = maior
    resposta["menor"] = menor
    resposta["media"] = soma / cont
    if mostra_situacao:
        if soma / cont > 5:
            resposta["situacao"] = "RUIM"
        elif soma / cont > 7:
            resposta["situacao"] = "RAZOÁVEL"
        else:
            resposta["situacao"] = "BOA"
    return resposta


resp = notas(5.5, 6.5, 7, mostra_situacao=True)
print(resp)