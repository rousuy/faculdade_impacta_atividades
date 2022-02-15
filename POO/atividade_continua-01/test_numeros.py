"""
Atenção: NÃO ENTREGUE ESSE ARQUIVO JUNTO COM A SUA SUBMISSÃO

Este é exemplo para testar as funções do módulo números,
aqui estão apenas alguns testes, que não incluem todos os testes
que serão realizados durante a correção. Mas se você implementou
a solução das funções e "passou" em todos os testes aqui, então
sua solução também deverá passar nos testes de correção.

Sinta-se a vontade para editar, comentar, adicionar ou excluir
partes desse arquivo, conforme julgar necessário.

* Copiem esse arquivo para a mesma pasta do arquivo numeros.py

* Para executá-lo, podem usar a seta verde no canto superior direito
ou então executar o comando seguinte no terminal:
	Windows: > py test_numeros.py
	Linux e Mac: $ python3 test_numeros.py
"""

import numeros


def print_cabecalho(titulo):
	n = len(titulo)
	print()
	print('#'*(n+6))
	print(f'# {titulo:^{n+2}} #')
	print('#'*(n+6))
	print()


def compara_respostas(funcao, testes, respostas):
	print('Entrada | Saída obtida | Saída esperada')
	padrao_saida = '{:^7} | {:^12} | {:^14}'
	for teste, resp in zip(testes, respostas):
		print(padrao_saida.format(
			teste,
			str(funcao(teste)),
			str(resp)
		))


# --------------------------------------------------------------------- #

pausar = input('Deseja pausar após cada teste? (s/n): ').lower() == 's'

# --------------------------------------------------------------------- #
print_cabecalho("função eh_primo")
testes = [7, 13, 19, 10, 15, 21]
respostas = [True, True, True, False, False, False]
compara_respostas(numeros.eh_primo, testes, respostas)

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_primos")
print('primos até 20:')
print('resposta obtida:  ', numeros.lista_primos(20))
print('resposta esperada:', [2, 3, 5, 7, 11, 13, 17, 19])

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função conta_primos")
d = numeros.conta_primos([11, 2, 3, 4, 11, 2, 5, 2])
resposta_esperada = {11: 2, 2: 3, 3: 1, 5: 1}
print('resposta obtida:  ', d)
print('resposta esperada:', resposta_esperada)
print('os dicionários são iguais?', d == resposta_esperada)

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_armstrong")
testes = [0, 5, 15, 28, 153]
respostas = [True, True, False, False, True]
compara_respostas(numeros.eh_armstrong, testes, respostas)

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_quase_armstrong")
testes = [0, 7, 35, 75, 153]
respostas = [False, False, True, True, False]
compara_respostas(numeros.eh_quase_armstrong, testes, respostas)

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_armstrong")
print('números de armstrong de 0 até 1000:')
print('resposta obtida:  ', numeros.lista_armstrong(1000))
print('resposta esperada:', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_perfeito")
testes = [4, 6, 12, 28, 350, 496]
respostas = [False, True, False, True, False, True]
compara_respostas(numeros.eh_perfeito, testes, respostas)

if pausar:
	input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_perfeitos")
print('números perfeitos de 2 até 1000:')
print('resposta obtida:  ', numeros.lista_perfeitos(1000))
print('resposta esperada:', [6, 28, 496])
