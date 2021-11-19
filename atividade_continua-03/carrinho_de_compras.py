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

# Atenção, caso queira copiar este código para o URI VOCÊ DEVE RETIRAR OS DOCS STRINGS E ANNOTATIONS!, CASO CONTRARIO,
# NÃO IRÁ PASSAR NO URI.

def adicionar(param1: list, param2: list) -> list:
    """
    Converte os valor do parâmetro 2 para inteiro, caso haja algum dado que não seja um número, este será
    desconsiderado, após, será incluido dentro da lista do carrinho.
    :param param1: list -> Carrinho os valores dos códigos do produto;
    :param param2: list -> Valores que contém os códigos à serem adicionados ao carrinho;
    :return: list -> retorna a lista do carrinho, com os códigos adicionados.
    """
    for i in param2:
        try:
            param1.append(int(i))
        except ValueError:
            pass
    return param1


def remover(param1: list, param2: str) -> list:
    """
    Remove o item do carrinho. Caso o código informado não esteja na lista do carrinho, este será desconsiderado, e
    será impresso uma mensagem ao usuário.
    :param param1: list -> Contêm os valores dos códigos dos produtos no carrinho;
    :param param2: str -> Recebe o input do usuário com o código do produto a ser removido, sendo convertido para int;
    :return: A lista atualizada com o código do produto removido, caso este esteja dentro do carrinho.
    """
    try:
        param1.remove(int(param2))
    except ValueError:
        print(f'código {param2} não encontrado')
    return param1


def exibir(param):
    for k, v in enumerate(sorted(param)):
        if k + 1 == len(param):
            print(v)
        else:
            print(v, end=' ')


code_list = []
code1 = input().split()
if code1 != '':
    adicionar(code_list, code1)
while True:
    code2 = input().split()
    if code2[0] == 'adicionar':
        adicionar(code_list, code2)
    elif code2[0] == 'remover':
        remover(code_list, code2[1])
    elif code2[0] == 'exibir':
        exibir(code_list)
    elif code2[0] == 'encerrar':
        exibir(code_list)
        break
