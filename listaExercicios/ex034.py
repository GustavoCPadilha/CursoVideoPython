"""
Aumentos múltiplos
"""

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    print(f'Quem ganhava R${salario} passa a ganhar R${salario*(15/100)+salario}')
else:
    print(f'Quem ganhava R${salario} passa a ganhar R${salario*(10/100)+salario}')