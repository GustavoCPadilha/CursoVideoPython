"""
Radar eletrônico
"""

vel = int(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa}!')
print('Tenha um bom dia! Dirija com segurança!')