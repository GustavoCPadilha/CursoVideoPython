"""
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante a função input()
do Python, só que fazendo a validação para aceitar apenas
um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número válido.")
        if ok:
            break
    return valor


num = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {num}")