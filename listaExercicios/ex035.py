"""
Analisando Triângulo v1.0
"""

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')


