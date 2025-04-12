"""
Verificando as primeiras letras de um texto (Se começa com "Santo")
"""
city = input('Em que cidade você nasceu? ').strip()
city = city.lower()
city_words = city.split()
if city_words[0] == "santo":
    print(True)
else:
    print(False)