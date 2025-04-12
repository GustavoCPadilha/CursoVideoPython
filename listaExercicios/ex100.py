"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""
from random import randint
from time import sleep

numeros = []

def sorteia():
    print("Sorteando 5 valores da lista:", end=' ')
    for i in range(0, 5):
        aleatorio = randint(0, 10)
        print(f"{aleatorio}", end=' ')
        sleep(0.4)
        numeros.append(aleatorio)
    print("PRONTO!")

def soma_par():
    soma = 0
    for i in range(0, 5):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f"Somando os valores pares de {numeros}, temos {soma}")


sorteia()
soma_par()