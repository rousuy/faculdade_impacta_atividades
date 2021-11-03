"""
Os números primos têm diversas aplicações, principalmente na criptografia utilizada pelo aplicativo de seu banco e nos
sites de compra que nos trazem tanta comodidade.

Um número natural é considerado primo quando possui somente dois divisores, o número um e ele próprio. O número zero
e o número um não são primos e o número dois é o único primo par.

Seu objetivo é criar um programa que receba como entrada dois números naturais, INÍCIO e FIM, e exibe os números primos
que existem no intervalo fechado [ INÍCIO..FIM ]. Ao final, o programa também deve exibir a quantidade de primos
encontrados no intervalo.

Entrada
Dois números naturais, INÍCIO e FIM, respectivamente, um por linha. Adote (INICIO <= FIM <= 5000).

Saída
Os números primos presentes no intervalo fechado [ INÍCIO..FIM ] e a quantidade de números primos do intervalo,
conforme o padrão exibido nos exemplos.
"""
# Resposta Utilizando o laço de repetição for:
inicio = int(input())
fim = int(input())
primos = 0
while inicio <= fim:
    divisiveis = 0
    for num in range(1, inicio + 1):
        if inicio % num == 0:
            divisiveis += 1
    if divisiveis <= 2:
        print(inicio)
        primos += 1
    inicio += 1
print(f'primos: {primos}')

# Resposta utilizando o laço de repetição while:
inicio = int(input())
fim = int(input())
primos = 0
while inicio <= fim:
    divisiveis = 0
    contador = 1
    while contador <= inicio:
        if inicio % contador == 0:
            divisiveis += 1
        contador += 1
    if divisiveis == 2:
        print(inicio)
        primos += 1
    inicio += 1
print(f'primos: {primos}')
