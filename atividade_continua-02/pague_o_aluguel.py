"""
Ramón está com problemas para pagar o aluguel de sua casa, o pior é que total da dívida é enorme, pois ele tem muitos
pagamentos em atraso, atualmente são mais de 14 meses atrasados!

A casa de Ramón está em uma vila em que todas as casas pertencem a uma única pessoa, o Senhor Édgar. Para quitar a
dívida, Ramón fez um acordo com Senhor Édgar, prometendo pagar mensalmente um valor que será descontado da dívida total.
Ele se comprometeu a sempre pagar o mesmo valor até que a dívida seja encerrada. Porém, se o valor que ele puder pagar
superar o valor da dívida, ele pagará exatamente o que deve e não mais, evidentemente.

Como Ramón não tem um controle adequado para atualizar o valor da dívida de acordo com os valores pagos, pediu sua
ajuda para construir um programa que receba como entrada o valor da dívida e o valor que se comprometeu a pagar
mensalmente, o programa deve exibir, mês a mês, o valor da dívida antes e depois do pagamento.

Entrada
Dois números inteiros positivos, o primeiro representa o valor total da dívida e o segundo o valor que Ramón poderá
pagar mensalmente.

Saída
O número do pagamento, o valor restante da dívida antes do pagamento mensal e o valor restante da dívida após o
pagamento mensal, conforme o padrão exibido nos exemplos. A exibição deve continuar até que a dívida seja quitada.
"""

# Resposta utilizando laços de repetição for.... Em questão de legibilidade e performance do algoritmo, este script
# não é o mais indicado?? No IDLE pycharm, a saída de dados, apresenta Runtime Error nos testes do URI....
valores = input().split()
divida, valor_pago = int(valores[0]), int(valores[1])
if divida > valor_pago:
    for key, value in enumerate(range(divida, -valor_pago, -valor_pago)):
        print(f'pagamento: {key + 1}\nantes = {value}')
        if value >= valor_pago:
            print(f'depois = {value - valor_pago}\n-----')
        else:
            print(f'depois = {value -value}\n-----')
            break
else:
    print(f'pagamento: {1}\nantes = {divida}\ndepois = {divida - divida}\n-----')


# Resposta utilizando laços de repetição while....Em relação de legibilidade e simplicidade, acredito que este
# Algoritmo seja mais recomendado do que o for?........Este também está dando Runtime Error no URI.
valores = input().split()
divida, valor_pago = int(valores[0]), int(valores[1])
contador = 1
if divida > valor_pago:
    while True:
        print(f'pagamento: {contador}\nantes = {divida}\ndepois = {divida - valor_pago}\n-----')
        divida -= valor_pago
        contador += 1
        if divida < valor_pago:
            print(f'pagamento: {contador}\nantes = {divida}\ndepois = {divida - divida}\n-----')
            break
print(f'pagamento: {contador}\nantes = {divida}\ndepois = {divida - divida}\n-----')
