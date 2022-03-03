import pytest
from atividade_conta import Conta


@pytest.mark.parametrize('atributo', ['_Conta__titular', '_Conta__agencia', 
'_Conta__numero', '_Conta__saldo', '_Conta__ativa', '_Conta__operacoes'])
def test_cria_conta(atributo):
	try:
		cc = Conta('Maria', 3000, 12345, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	else:
		mensagens_atributos = {'_Conta__titular': 'Não criou o atributo privado titular',
		'_Conta__agencia':'Não criou o atributo privado agencia',
		'_Conta__numero':'Não criou o atributo privado numero',
		'_Conta__saldo':'Não criou o atributo privado saldo',
		'_Conta__ativa':'Não criou o atributo privado ativa',
		'_Conta__operacoes':'Não criou o atributo privado operacoes'}
		assert hasattr(cc, atributo), mensagens_atributos[atributo]
		

@pytest.mark.parametrize('titular', ['Maria', 'Pedro', 'Joao'])
def test_conta_titular(titular):
	try:
		cc = Conta(titular, 3000, 12345, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		assert hasattr(cc, "_Conta__titular"), "A classe Conta não possui o atributo privado titular"
		assert cc._Conta__titular == titular and cc.titular == titular
	except:
		raise AssertionError('Conta criada com titular incorreto e/ou erro de implementação na property titular')


@pytest.mark.parametrize('agencia', [1234, 6681])
def test_conta_agencia(agencia):
	try:
		cc = Conta('Maria', agencia, 12345, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		assert hasattr(cc, "_Conta__agencia"), "A classe Conta não possui o atributo privado agencia"
		assert cc._Conta__agencia == agencia and cc.agencia == agencia
	except:
		raise AssertionError('Conta criada com agencia incorreta e/ou erro de implementação na property agencia')


@pytest.mark.parametrize('numero', [29282, 35389])
def test_conta_numero(numero):
	try:
		cc = Conta('Maria', 3000, numero, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		assert hasattr(cc, "_Conta__numero"), "A classe Conta não possui o atributo privado numero"
		assert cc._Conta__numero == numero and cc.numero == numero
	except:
		raise AssertionError('Conta criada com numero incorreto e/ou erro de implementação na property numero')


@pytest.mark.parametrize('saldo', [100, 200])
def test_conta_saldo(saldo):
	try:
		cc = Conta('Maria', 3000, 12345, saldo)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		assert hasattr(cc, "_Conta__saldo"), "A classe Conta não possui o atributo privado saldo"
		assert cc._Conta__saldo == saldo and cc.saldo == saldo
	except:
		raise AssertionError('Conta criada com saldo incorreto e/ou erro de implementação na property saldo')


@pytest.mark.parametrize('ativa', [True, False])
def test_conta_ativa(ativa):
	try:
		cc = Conta('Maria', 3000, 12345, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		assert hasattr(cc, "_Conta__ativa"), "A classe Conta não possui o atributo privado ativa"
		cc._Conta__ativa = ativa
		assert cc.ativa == ativa
	except:
		raise AssertionError('Erro de implementação na property ativa')


@pytest.mark.parametrize('valor', [True, False, 1, 'True', 'False'])
def test_conta_ativa_setter(valor):
	try:
		cc = Conta('Maria', 3000, 12345, 400)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.ativa = valor
		assert (isinstance(valor, bool) and cc.ativa == valor) or (not isinstance(valor, bool) and not cc.ativa)
	except:
		raise AssertionError('O setter ativa só deve aceitar valores booleanos')


@pytest.mark.parametrize('valor,checa_extrato', [(-300, False), (0, False), (300, False),
(-300, True), (0, True), (300, True)])
def test_conta_depositar_inativa(valor, checa_extrato):
	try:
		saldo_inicial = 400
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.depositar(valor)
	except Exception:
		raise AssertionError('Erro ao fazer depósito')
	else:
		assert cc.saldo == saldo_inicial, 'Não deve ser permitido depositar em uma conta inativa'
		if checa_extrato:
			assert hasattr(cc, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
			assert len(cc._Conta__operacoes) == 1, 'Depósito com conta inativa registrado na lista de operações'


@pytest.mark.parametrize('valor,checa_extrato', [(-300, False), (0, False), (300, False),
(-300, True), (0, True), (300, True)])
def test_conta_depositar_ativa(valor, checa_extrato):
	try:
		saldo_inicial = 400
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
		cc.ativa = True
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.depositar(valor)
	except Exception:
		raise AssertionError('Erro ao fazer depósito')
	else:
		if valor <= 0:
			assert cc.saldo == saldo_inicial, 'Não deve ser permitido depositar valores negativos ou iguais a zero'
			if checa_extrato:
				assert hasattr(cc, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
				assert len(cc._Conta__operacoes) == 1, 'Depósito com valor negativo ou igual a zero registrado na lista de operações'
		else:
			assert cc.saldo == saldo_inicial + valor, 'O saldo da conta não foi atualizado corretamente após o depósito'
			if checa_extrato:
				assert hasattr(cc, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
				assert cc._Conta__operacoes[-1] == ('deposito', valor), 'Depósito não registrado na lista de operações'


@pytest.mark.parametrize('valor,checa_extrato', [(-300, False), (0, False), (300, False),
(-300, True), (0, True), (300, True)])
def test_conta_sacar_inativa(valor, checa_extrato):
	try:
		saldo_inicial = 400
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.sacar(valor)
	except Exception:
		raise AssertionError('Erro ao fazer depósito')
	else:
		assert cc.saldo == saldo_inicial, 'Não deve ser permitido sacar em uma conta inativa'
		if checa_extrato:
			assert hasattr(cc, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
			assert len(cc._Conta__operacoes) == 1, 'Saque com conta inativa registrado na lista de operações'


@pytest.mark.parametrize('valor,checa_extrato', [(-300, False), (0, False), (300, False), (500, False),
(-300, True), (0, True), (300, True), (400, False), (400, True), (500, True)])
def test_conta_sacar_ativa(valor, checa_extrato):
	try:
		saldo_inicial = 400
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
		cc.ativa = True
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.sacar(valor)
	except Exception:
		raise AssertionError('Erro ao sacar')
	else:
		if checa_extrato:
			assert hasattr(cc, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
		if valor <= 0:
			assert cc.saldo == saldo_inicial, 'Não deve ser permitido sacar valores negativos ou iguais a zero'
			if checa_extrato:
				assert len(cc._Conta__operacoes) == 1, 'Saque com valor negativo ou igual a zero registrado na lista de operações'
		elif valor > saldo_inicial:
			assert cc.saldo == saldo_inicial, 'Não deve ser permitido sacar valores maiores que o saldo da conta'
			if checa_extrato:
				assert len(cc._Conta__operacoes) == 1, 'Saque com valor maior que o saldo registrado na lista de operações'
		else:
			assert cc.saldo == saldo_inicial - valor, 'O saldo da conta não foi atualizado corretamente após o depósito'
			if checa_extrato:
				assert cc._Conta__operacoes[-1] == ('saque', valor), 'Depósito não registrado na lista de operações'


@pytest.mark.parametrize('valor,checa_extrato,ativa_origem,ativa_destino', 
[(300, True, False, False), (300, True, False, True), (300, True, True, False), 
(-300, False, True, True), (0, False, True, True), (0, True, True, True),
(300, False, True, True), (300, True, True, True),
(400, False, True, True), (400, True, True, True),
(500, False, True, True), (500, True, True, True)])
def test_conta_transferir(valor, checa_extrato, ativa_origem, ativa_destino):
	try:
		saldo_inicial_1 = 400
		c1 = Conta('Maria', 3000, 12345, saldo_inicial_1)
		saldo_inicial_2 = 400
		c2 = Conta('Pedro', 4456, 92176, saldo_inicial_2)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		c1.ativa = ativa_origem
		c2.ativa = ativa_destino
		c1.transferir(c2, valor)
	except Exception:
		raise AssertionError('Erro ao fazer transferencia')
	else:
		if checa_extrato:
			assert hasattr(c1, "_Conta__operacoes"), "A classe Conta não possui o atributo privado operacoes"
		if not ativa_origem or not ativa_destino:
			assert c1.saldo == saldo_inicial_1 and c2.saldo == saldo_inicial_2, 'Não deve ser permitido fazer uma transferência se uma das contas não está ativa'
			if checa_extrato:
				assert len(c1._Conta__operacoes) == 1, 'A transferência não deve ser registrada na lista de operações caso uma das contas esteja inativa'
		elif ativa_origem and ativa_destino and valor <= 0:
			assert c1.saldo == saldo_inicial_1 and c2.saldo == saldo_inicial_2, 'Não deve ser permitido fazer uma transferência com valor negativo ou igual a zero'
			if checa_extrato:
				assert len(c1._Conta__operacoes) == 1, 'A transferência não deve ser registrada na lista de operações caso o valor seja negativo ou igual a zero'
		elif ativa_origem and ativa_destino and valor > saldo_inicial_1:
			assert c1.saldo == saldo_inicial_1 and c2.saldo == saldo_inicial_2, 'Não deve ser permitido fazer uma transferência se o valor ultrapassar o saldo da conta de origem'
			if checa_extrato:
				assert len(c1._Conta__operacoes) == 1, 'A transferência não deve ser registrada na lista de operações caso o valor ultrapasse o saldo da conta de origem'
		elif ativa_origem and ativa_destino and valor > 0 and valor <= saldo_inicial_1:
			assert c1.saldo == (saldo_inicial_1 - valor) and c2.saldo == (saldo_inicial_2 + valor), 'A transferência deve descontar o valor do saldo da conta original e acrescentar o valor ao saldo da conta de destino'
			if checa_extrato:
				assert c1._Conta__operacoes[-1] == ('transferencia', valor), 'Transferência não registrada na lista de operações'


def test_conta_tirar_extrato_sem_operacoes():
	try:
		saldo_inicial = 500
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	else:
		lista = cc.tirar_extrato()
		assert isinstance(lista, list), 'O resultado do método tirar_extrato() deve ser do tipo list'
		assert len(lista) == 1, 'O método tirar_extrato() retorna uma lista de operações com valores diferentes aos esperados'
		assert lista[0] == ('saldo inicial', saldo_inicial), 'O método tirar_extrato() retorna uma lista de operações com valores diferentes aos esperados'	


def test_conta_tirar_extrato_apos_operacoes():
	try:
		saldo_inicial = 500
		cc = Conta('Maria', 3000, 12345, saldo_inicial)
	except Exception:
		raise AssertionError('Erro no construtor da classe Conta')
	try:
		cc.ativa = True
		cc.depositar(200)
		cc.sacar(100)	
	except Exception:
		raise AssertionError('Erro ao manipular a lista de operações')
	else:
		lista = cc.tirar_extrato()
		assert isinstance(lista, list), 'O resultado do método tirar_extrato() deve ser do tipo list'
		if len(lista) == 3:
			assert lista[0] == ('saldo inicial', saldo_inicial) and lista[1] == ('deposito', 200) and lista[2] == ('saque', 100), 'O método tirar_extrato() retorna uma lista de operações com valores diferentes aos esperados'
		else:
			raise AssertionError('O método tirar_extrato() retorna uma lista de operações com valores diferentes aos esperados')	


if __name__ == '__main__':
	pytest.main()
