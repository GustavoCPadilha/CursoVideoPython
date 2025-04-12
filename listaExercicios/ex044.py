"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
print("="*10, "LOJAS GUKA", "="*10)
preco = float(input("Preço das compras: "))
print("FORMA DE PAGAMENTO\n"
      "[ 1 ] à vista dinheiro/cheque\n"
      "[ 2 ] à vista no cartão\n"
      "[ 3 ] 2x no cartão\n"
      "[ 4 ] 3x ou mais no cartão")
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print(f"Sua compra de R${preco} vai custar {preco - preco*(10/100)}")
elif opcao == 2:
    print(f"Sua compra de R${preco} vai custar {preco - preco * (5/100)}")
elif opcao == 3:
    print(f"Sua compra será parcelada em 2X de {preco/2} SEM JUROS")
elif opcao == 4:
    parcela = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcela}X de {preco/parcela} COM JUROS")
    print(f"Sua compra de R${preco} vai custar {preco + preco * (20/100)}")
else:
    print("Opção inválida, tente novamente.")
