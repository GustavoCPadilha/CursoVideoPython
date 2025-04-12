sexo = input('Informe seu sexo [M/F]:').strip().upper()[0]

while sexo != "M" and sexo != "F":
    print('Dados inválidos. Por favor, informe seu sexo:')
    sexo = input('Informe seu sexo [M/F]:').strip().upper()[0] 
print(f'Sexo {sexo} registrado com sucesso')