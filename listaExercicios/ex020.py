import random

nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f"A ordem de apresentação será:"
      f"{lista}")