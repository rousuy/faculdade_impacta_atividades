"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
"""
# Resposta
num = input().split()
num1, num2 = int(num[0]), int(num[1])
if num1 % num2 == 0 or num2 % num1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
