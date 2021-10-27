"""
Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada
de N de 1 até 10.

Entrada
Um número natural N (0 <= N <= 10).

Saída
Exibir a tabuada do valor dado na entrada.
"""

# Resposta1 (usando estrutura com laço de repetição while):
num = int(input())
if 0 <= num <= 10:
    inicio = 1
    while inicio <= 10:
        print(f"{num} x {inicio} = {num * inicio}")
        inicio += 1

# Resposta2 (usando estrutura com laço de repetição for):
num = int(input())
if 0 <= num <= 10:
    for _ in range(1, 10):
        print(f"{num} x {_} = {num * _}")
