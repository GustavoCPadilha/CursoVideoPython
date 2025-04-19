def leia_dinheiro(msg):
    ok = False
    valor = ''
    texto = input(msg).replace(",", ".").strip()
    while not ok:
        for letra in texto:
            if letra in '1234567890.':
                valor += letra
            else:
                print(f'ERRO: "{texto}" é um preço inválido!')
                texto = input(msg).strip()
        ok = True
    return float(valor)