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

# Atenção, caso queira copiar este código para o URI VOCÊ DEVE RETIRAR OS DOCS STRINGS E ANNOTATIONS!, CASO CONTRARIO,
# NÃO IRÁ PASSAR NO URI.


def calcula_tabuada(x: int, y: int) -> print():
    """
    Imprimi a tabuada de acordo com os números passados para x e y, caso x seja maior que y, será desconsiderado, senão,
    caso números positivos, será impressa a tabuada na respectiva ordem do intervalo, caso os números sejam negativos,
    também será impressa a tabuada em ordem crescente, até que o valor seja igual a 10.
    :param x: int -> Valores positivos ou negativos menores que y
    :param y: int -> Valores positivos ou negativos maiores que x
    :return: None
    """
    if x <= y:
        while x <= y:
            contador = 1
            while contador <= 10:
                print(f'{x} x {contador} = {x * contador}')
                contador += 1
            print('-' * 10)
            x += 1
    else:
        print('Nenhuma tabuada no intervalo!')


foo = int(input())
bar = int(input())
calcula_tabuada(foo, bar)
