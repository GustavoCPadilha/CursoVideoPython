import math

angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno}")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno}")
print(f"O ângulo de {angulo} tem o TANGENTE de {tangente}")