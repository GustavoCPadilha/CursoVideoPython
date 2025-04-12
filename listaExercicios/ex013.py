salario = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${(15*salario) / 100 + salario:.2f}')
