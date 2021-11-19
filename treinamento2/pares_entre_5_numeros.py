"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
"""
# Resposta utilizando laços de repetição e variável acumuladora:

pares = 0
for _ in range(5):
    num = int(input())
    if num % 2 == 0:
        pares += 1
print(f'{pares} valores pares')


# Resposta utilizando estrutura de seleção encadeada e variável acumuladora:
pares = 0
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
if num1 % 2 == 0:
    pares += 1
elif num2 % 2 == 0:
    pares += 1
elif num3 % 2 == 0:
    pares += 1
elif num4 % 2 == 0:
    pares += 1
elif num5 % 2 == 0:
    pares += 1
print(f'{pares} valores pares')
