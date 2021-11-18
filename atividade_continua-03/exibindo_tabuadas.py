"""
Escreva um programa que receba como entrada dois números inteiros quaisquer A e B e exiba todas as tabuadas existentes
no intervalo fechado crescente [ A..B ].

Entrada
Dois números inteiros, um em cada linha.

Saída
As tabuadas de todos os valores inteiros no intervalo fechado crescente [ A..B ]. Ao fim de cada tabuada, exibir uma
linha com dez hifens ('-'). Caso A seja maior do que B, o intervalo será vazio e, neste caso, deve ser exibida somente
a frase 'Nenhuma tabuada no intervalo!', sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.
"""
# Resposta:


def calcula_tabuada(x, y):
    if x <= y:
        while x <= y:
            contador = 1
            while contador <= 10:
                print(f'{x} x {contador} = {x * contador}')
                contador += 1
            print('-' * 10)
            x += 1
    elif x >= y and y < 0 < x:
        while x >= y:
            contador = 1
            while contador <= x:
                print(f'{x} x {contador} = {x * contador}')
                contador += 1
            print('-' * 10)
            x -= 1
    else:
        print('Nenhuma tabuada no intervalo')


foo = int(input())
bar = int(input())
calcula_tabuada(foo, bar)
