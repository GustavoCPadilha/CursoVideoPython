def aumentar(valor = 0, acrescimo = 0, formatado = False):
    acrescimo /= 100
    resposta = valor + valor * acrescimo
    if not formatado:
        return resposta
    else:
        return moeda(resposta)

def diminuir(valor = 0, reducao = 0, formatado = False):
    reducao /= 100
    resposta = valor - valor * reducao
    if not formatado:
        return resposta
    else:
        return moeda(resposta)

def dobro(valor = 0, formatado = False):
    resposta = valor * 2
    if not formatado:
        return resposta
    else:
        return moeda(resposta)

def metade(valor = 0, formatado = False):
    resposta = valor / 2
    if not formatado:
        return resposta
    else:
        return moeda(resposta)

def moeda(valor: float = 0, tipo_moeda = "R$"):
    return f"{tipo_moeda}{valor:.2f}".replace(".",",")

def resumo(valor = 0, acrescimo = 0, reducao = 0):
    print('-' * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-' * 30)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{moeda(dobro(valor))}")
    print(f"Metade do preço: \t{moeda(metade(valor))}")
    print(f"{acrescimo}% de aumento: \t{moeda(aumentar(valor))}")
    print(f"{reducao}% de redução: \t{moeda(diminuir(valor))}")
    print('-' * 30)
