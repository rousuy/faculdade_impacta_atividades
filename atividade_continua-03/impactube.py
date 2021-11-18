"""
A ImpacTube, uma famosa empresa de compartilhamento de vídeos, quer premiar alguns de seus mais notáveis criadores de
conteúdo. Para isso, a ImpacTube montará uma tabela com alguns dos canais que possuem grande quantidade de usuários
inscritos.

No site da ImpacTube, os canais geram renda para seus criadores de conteúdo por meio de diversos mecanismos, a conhecida
 "monetização", o que geralmente é influenciado pela quantidade de inscritos no canal e que acessam aos vídeos postados.

Para possibilitar a premiação, cada registro da tabela terá quatro campos dispostos em
colunas na seguinte ordem:

1 - O nome do canal;
2 - A quantidade atual de inscritos;
3 - A monetização do último mês do canal e;
4 - Um valor indicando se o canal produz conteúdo premium, que são vídeos exclusivos para usuários que pagam uma
mensalidade à ImpacTube.

Com esses dados será possível definir a bonificação de cada canal, que será composta pelo valor "monetização" da tabela
acrescido de um valor fixo para cada mil inscritos.  O valor fixo será definido pela ImpacTube, sendo X para canais com
conteúdo premium e Y para os que não possuem conteúdo premium.

Você foi escolhido para desenvolver um programa que receberá como entrada os dados de cada canal, gerando internamente
a tabela modelo, e que mostrará os nomes dos canais, na ordem em que foram dados na entrada, acompanhados do valor que
receberão como bonificação. Observe cuidadosamente o formato de entrada e o formato de saída especificados.

Entrada
Na primeira linha será informado um número inteiro que representa a quantidade N (1 <= N <= 200) de canais da tabela;
Em cada uma das N linhas seguintes serão informados os registros que compõem a tabela, com os valores das colunas
separados por um ponto e vírgula, nesta ordem: (1) uma string com o nome do canal que será bonificado; (2) um número
natural que é a quantidade de inscritos no canal; (3) um número real simbolizando a monetização do canal no mês anterior
(dado em reais R$) e; (4) uma string 'sim' ou 'não', sem apóstrofos e completamente em minúsculo, que indica se o canal
produz conteúdo premium;Por fim, serão informados dois números reais X e Y, um em cada linha, que indicam o valor fixo
(em reais R$) que os canais receberão a mais para cada mil inscritos no canal. O primeiro valor é X e refere-se aos
canais que possuem conteúdo premium. O segundo valor é Y e refere-se aos canais que não possuem conteúdo premium.

Saída
O cabeçalho contém três linhas, sendo a primeira e a terceira compostas por apenas cinco hifens, e a segunda composta
unicamente pela palavra 'BÔNUS', sem apóstrofos e completamente em maiúsculo. Nas próximas N linhas, estão os nomes dos
canais, na mesma ordem em que foram dados na entrada, acompanhados à direita pelo valor que receberão como bonificação,
em reais e com duas casas decimais, exatamente como consta nos exemplos.
"""


# Resposta:

# Cabeçalho
def header():
    print(f'{"-" * 5}\nBÔNUS\n{"-" * 5}')


def payment_out(param1):
    header()
    for i in param1:
        print(f'{i[0]}: ', end='')
        print(f'R$ {i[1]:.2f}')


def payment_calculator(p1, p2, p3):
    payment_calculate = []
    for i in p1:
        if i[1] > 999:
            if 'sim' in i[3]:
                pre_payment = [i[0], ((i[1] // 1000) * p2) + i[2]]
                payment_calculate.append(pre_payment)
            else:
                pre_payment = [i[0], ((i[1] // 1000) * p3) + i[2]]
                payment_calculate.append(pre_payment)
        else:
            pre_payment = [i[0], i[2]]
            payment_calculate.append(pre_payment)
    return payment_calculate


full_table = []
table_size = int(input())
count = 1
while count <= table_size:
    data = input().split(';')
    channel_name = str(data[0]).strip()
    qtd_inscriptions = int(data[1])
    monetization = float(data[2])
    premium_content = str(data[3]).strip().lower()
    table = [channel_name, qtd_inscriptions, monetization, premium_content]
    full_table.append(table)
    count += 1

x = float(input())
y = float(input())
payment = payment_calculator(full_table, x, y)
payment_out(payment)
