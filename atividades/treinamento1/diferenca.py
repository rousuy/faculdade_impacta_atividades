"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de
C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas
"""

# Resposta:
lista = []
for value in range(0, 4):
    lista.append(int(input()))
A, B, C, D = lista
diferenca = (A*B) - (C*D)
print(f"DIFERENCA = {diferenca}")
