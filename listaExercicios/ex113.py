"""
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leia_int(msg):
    num = 0
    ok = False
    while not ok:
        try:
            num = int(input(msg))
            ok = True
        except ValueError:
            print("ERRO: por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("O usuário preferiu não informar um número")
            return 0
    return num


def leia_float(msg):
    num = 0
    ok = False
    while not ok:
        try:
            num = float(input(msg))
            ok = True
        except ValueError:
            print("ERRO: por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("O usuário preferiu não informar um número")
            return 0
    return num


inteiro = leia_int("Digite um número inteiro: ")
real = leia_float("Digite um número real: ")
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}")