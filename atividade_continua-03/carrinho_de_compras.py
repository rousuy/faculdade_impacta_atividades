"""
Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho.
Cada item é representado no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo
unicamente. Como solução inicial, você decidiu guardar os itens adicionados ao carrinho em uma lista, e para testar o
seu programa, implementou alguns básicos para simular uma interação do usuário com o sistema:

adicionar: inclui o código de um novo produto à lista;
remover: remove o código de um produto da lista;exibir: exibe os itens da lista em ordem crescente;
encerrar: exibe os itens da lista, assim como no comando exibir, em ordem crescente,
e encerra o programa.

A primeira linha poderá conter uma lista de inteiros separados por espaços, representando produtos que já estavam no
carrinho, por exemplo, de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa
lista e inicializar o carrinho de compras já com os códigos dessa lista, que devem ser números inteiros.

Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum
texto ou caractere.

Entrada
A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;
Cada linha seguinte conterá um dos comandos listados acima e, para os comandos "adicionar" e "remover", conterá também
o código de um produto separado por um espaço;
A entrada termina sempre com o comando "encerrar".

Saída
A saída deve conter:
A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandos "exibir" e "encerrar";
A mensagem "código <código> não encontrado", quando o comando remover é executado com um código que não esteja presente
na lista. Substitua <código> pelo número do código em questão (veja os exemplos para maiores detalhes).

Obs.: Lembre-se de não exibir texto no input.
"""


# Resposta:


def adicionar(param, param2):
    param2.append(param)
    return


def remover(param1, param2):
    try:
        param1.remove(param2)
    except ValueError:
        print(f'código {param2} não encontrado')
    return


def exibir(param):
    param.sort()
    count = 0
    for i in param:
        count += 1
        if count == len(param):
            print(i)
        else:
            print(i, end=' ')


cod_list = []
codigo1 = input().split()
if codigo1 != '':
    codigo1 = [adicionar(int(i), cod_list) for i in codigo1]
while True:
    codigo2 = input().split()
    if codigo2[0] == 'adicionar':
        adicionar(int(codigo2[1]), cod_list)
    elif codigo2[0] == 'remover':
        remover(cod_list, int(codigo2[1]))
    elif codigo2[0] == 'exibir':
        exibir(cod_list)
    elif codigo2[0] == 'encerrar':
        exibir(cod_list)
        break
