"""
Forrest é um garoto que adora correr e contar histórias, as vezes até conta histórias sobre correr... vai entender. Como
costuma correr diariamente pela cidade, Forrest sempre procura fazer o menor tempo possível, porém não é muito
organizado e anota os tempos de suas corridas em papeis que são jogados em sua gaveta sem nenhum tipo de ordenação.

Como Forrest está muito ocupado ultimamente, planejando como cumprir uma promessa a um antigo amigo que adorava
restaurantes e camarão, pediu a você que crie um programa que receba como entrada os tempos das corridas que estão nos
papeis e calcule a média aritmética dos tempos gastos por ele para completar o seu percurso de corrida diário. Ao final,
seu programa deve também exibir todos os tempos de corrida abaixo dessa média, na mesma ordem em que foram recebidos na
entrada.

Entrada
Diversos valores inteiros, um por linha, que representam os tempos gastos em cada corrida (em segundos);A entrada é
finalizada com a inserção de um valor negativo, que não deve ser contabilizado.

Saída

Na primeira linha a palavra 'MEDIA', sem apóstrofos, sem acentuação e completamente em maiúsculo, seguida por dois
pontos (':'), um caractere de espaço e um valor real com duas casas decimais, indicando a média dos tempos dados na
entrada, em segundos;Nas linhas seguintes, os tempos de corrida abaixo da média calculada, em segundos, um por linha e
na mesma ordem em que foram dados na entrada.
"""
# Resposta:


def average_calculator(param: list) -> vars:
    """
    Calcula a média aritmética das corridas
    :param param: List -> Recebe os valores das corridas;
    :return: var -> Retorna uma variável a média das corridas
    """
    average_t = sum(param) / len(param)
    return average_t


def average_output(param1: list, param2: vars) -> print():
    """
    Imprimi a média das corridas, caso alguma das corridas, sejam inferior ao valor da média, esta também será impressa.
    :param param1: list -> Recebe os valores da corridas;
    :param param2: var -> Recebe o valor da média
    :return:
    """
    print(f'MEDIA: {param2:.2f}')
    for i in param1:
        if i < param2:
            print(i)


runs = []
count = 0
while True:
    time = int(input())
    if time < 0:
        break
    else:
        runs.append(time)
        count += time
average = average_calculator(runs)
average_output(runs, average)
