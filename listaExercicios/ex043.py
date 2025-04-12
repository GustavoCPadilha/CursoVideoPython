"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (M)'))
imc = peso/(altura*altura)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('IMC abaixo de 18,5: Abaixo do Peso')
elif 18.5 <= imc <= 25:
    print('Entre 18,5 e 25: Peso Ideal')
elif 25.1 <= imc <= 30:
    print('25 até 30: Sobrepeso')
elif 30.1 <= imc <= 40:
    print('30 até 40: Obesidade')
else:
    print('Acima de 40: Obesidade Mórbida')
