from time import sleep

def linha():
    print("-" * 30)

def menu():
    linha()
    print(f'{"MENU PRINCIPAL":^30}')
    linha()
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do sistema")
    linha()

def ler_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            while opcao not in [1, 2, 3]:
                print("ERRO: Por favor, digite uma opção válida.")
                opcao = int(input(msg))
            break
        except ValueError:
            print("ERRO: Por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("\nO usuário preferiu não informar a opção...")
            opcao = 3
            break
    linha()
    return opcao
