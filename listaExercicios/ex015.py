dias_alugados = int(input("Quantos dias alugados? "))
km_rodado = float(input("Quantos km rodados? "))
valor_dia = dias_alugados * 60
valor_km = km_rodado * 0.15
print(f"O total a pagar é de R${valor_dia + valor_km}")