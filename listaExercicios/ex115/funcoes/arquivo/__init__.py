from time import sleep

def arquivo_existe(nome):
    try:
        with open(nome, "rt"):
            return True
    except FileNotFoundError:
        return False

def criar_arquivo(nome):
    try:
        with open(nome, "wt+"):
            pass
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def ler_arquivo(nome):
    try:
        with open(nome, "rt") as arquivo:
            print(f"{'NOME':<30}{'IDADE':>5}")
            print("-" * 35)
            for linha in arquivo:
                dado = linha.strip().split(';')
                if len(dado) >= 2:
                    print(f"{dado[0]:<30}{dado[1]:>5} anos")
    except:
        print("Erro ao ler o arquivo!")
    sleep(2)

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f"{nome};{idade}\n")
    except:
        print("Houve um erro na hora de escrever os dados!")
    else:
        print(f"Novo registro de {nome} adicionado.")
