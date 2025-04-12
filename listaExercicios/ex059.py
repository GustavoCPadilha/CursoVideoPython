"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('    [ 1 ] somar\n'
          '    [ 2 ] multiplicar\n'
          '    [ 3 ] maior\n'
          '    [ 4 ] novos números\n'
          '    [ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {num1} + {num2} é {num1+num2}')
    elif opcao == 2:
        print(f'O resultado de {num1} x {num2} é {num1*num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}')
        else:
            print(f'Entre {num1} e {num2} o maior valor é {num2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa! Volte sempre!')