"""
Aprovando Empréstimo
"""

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
parcela = casa / meses

if parcela <= (30/100) * salario:
    print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${parcela:.2f}')
    print('Empréstimo CONCEDIDO!')
else:
    print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${parcela:.2f}')
    print('Empréstimo NEGADO!')
