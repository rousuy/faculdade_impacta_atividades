"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com
mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos
após o ponto decimal.
"""

# Resposta:
A = float(input())
B = float(input())
C = float(input())
a1 = (A * C) / 2
b2 = 3.14159 * C ** 2
c3 = ((A + B) / 2) * C
d4 = B ** 2
e5 = A * B
print(f"TRIANGULO: {a1:.3f}\nCIRCULO: {b2:.3f}\nTRAPEZIO: {c3:.3f}\nQUADRADO: {d4:.3f}\nRETANGULO: {e5:.3f}")
