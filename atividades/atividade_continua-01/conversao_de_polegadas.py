"""
Megan quer comprar um novíssimo smartphone e está muito empolgada com as possibilidades que uma tela de tantas
polegadas pode oferecer para seu entretenimento. Mas há um problema, Megan percebeu que não sabe lidar com polegadas,
afinal sempre realizou cálculos usando centímetros e gostaria de se basear nessa unidade de medida para imaginar o
tamanho de tela que comprará. Você pode ajudar Megan?

Seu trabalho é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas,
e exiba o equivalente em centímetros. Lembre-se que uma polegada equivale a 2,54 cm.

Entrada
Um número real representando as polegadas.

Saída
Um número real, com três casas decimais, representando a conversão das polegadas da entrada em centímetros.
"""

# Resposta:
pol = float(input())
cm = pol * 2.54
print(f"{cm:.3f}")
