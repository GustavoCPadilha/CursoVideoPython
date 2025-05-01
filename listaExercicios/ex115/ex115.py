from ListaExercicios.ex115.funcoes.interface import *
from ListaExercicios.ex115.funcoes.arquivo import *

arquivo = "funcoes/arquivo/cursoemvideo.txt"

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    menu()
    opcao = ler_opcao("Sua opção: ")
    if opcao == 1:
        ler_arquivo(arquivo)
    elif opcao == 2:
        print(f'{"CADASTRAR NOVA PESSOA":^30}')
        nome = input("Nome: ")
        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Idade inválida. Cadastro cancelado.")
        else:
            cadastrar(arquivo, nome, idade)
    elif opcao == 3:
        print("Saindo do sistema... Até logo!")
        break
