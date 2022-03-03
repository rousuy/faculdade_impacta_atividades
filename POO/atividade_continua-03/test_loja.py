import pytest
import re
import loja


@pytest.mark.parametrize('atributo', ['_Produto__nome', '_Produto__preco'])
def test_cria_produto(atributo):
	try:
		prod = loja.Produto('Jogo online', 99)
	except Exception:
		raise AssertionError('Erro no construtor da classe Produto')
	else:
		mensagens_atributos = {'_Produto__nome': 'Não criou o atributo privado nome',
		'_Produto__preco':'Não criou o atributo privado preco'}
		assert hasattr(prod, atributo), mensagens_atributos[atributo]


@pytest.mark.parametrize('nome', ['Jogo', 'Microsoft Office'])
def test_produto_atributo_nome(nome):
	try:
		prod = loja.Produto(nome, 100)
		assert prod._Produto__nome == nome
	except Exception:
		raise AssertionError('Erro ao inicializar o atributo privado nome na classe Produto')


@pytest.mark.parametrize('nome', ['Jogo', 'Microsoft Office'])
def test_produto_property_nome(nome):
	try:
		prod = loja.Produto(nome, 100)
		assert prod.nome == nome
	except Exception:
		raise AssertionError('Erro no valor da property nome na classe Produto')


@pytest.mark.parametrize('preco', [100, 100.5])
def test_produto_preco_valido(preco):
	try:
		tipo = 'int' if isinstance(preco, int) else 'float' if isinstance(preco, float) else ''
		prod = loja.Produto('Jogo online', preco)
	except Exception:
		raise AssertionError('Erro ao criar Produto com preço do tipo {0}'.format(tipo))


def test_cria_produto_nome_vazio():
	try:
		prod = loja.Produto('', 30)
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError para Produto criado com nome vazio')
	else:
		raise AssertionError('Produto criado com nome vazio')


def test_produto_setter_nome_vazio():
	try:
		valor_inicial = 'abcdef'
		prod = loja.Produto(valor_inicial, 30)
		prod.nome = ''
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError no setter nome da classe Produto quando o nome é vazio')
	assert hasattr(prod, "_Produto__nome"), "A classe Produto não possui o atributo privado nome"
	assert prod._Produto__nome == valor_inicial, 'Não deve ser permitido alterar o valor do atributo privado nome quando o setter nome recebe uma string vazia'


@pytest.mark.parametrize('preco', ["", []])
def test_cria_produto_preco_invalido(preco):
	try:
		prod = loja.Produto('Jogo online', preco)
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError para Produto criado com preço que não é int nem float')
	else:
		raise AssertionError('Produto criado com preço inválido')


@pytest.mark.parametrize('preco', [-1, -3.0])
def test_cria_produto_preco_negativo(preco):
	try:
		prod = loja.Produto('Jogo online', preco)
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError para Produto criado com preço negativo')
	else:
		raise AssertionError('Produto criado com preço negativo')


@pytest.mark.parametrize('preco', ["", []])
def test_produto_setter_preco_invalido(preco):
	try:
		valor_inicial = 100
		prod = loja.Produto('Jogo online', valor_inicial)
		prod.preco = preco
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError no setter do preço quando o novo_preco não é int nem float')
	assert hasattr(prod, "_Produto__preco"), "A classe Produto não possui o atributo privado preco"
	assert prod._Produto__preco == valor_inicial, "O atributo privado preco não pode ter o seu valor inicial alterado caso o novo_preco seja inválido"


@pytest.mark.parametrize('preco', [-1, -3.0])
def test_produto_setter_preco_negativo(preco):
	try:
		valor_inicial = 100
		prod = loja.Produto('Jogo online', valor_inicial)
		prod.preco = preco
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError no setter do preço quando o novo_preco é negativo')
	assert hasattr(prod, "_Produto__preco"), "A classe Produto não possui o atributo privado preco"
	assert prod._Produto__preco == valor_inicial, "O atributo privado preco não pode ter o seu valor inicial alterado caso o novo_preco seja negativo"


@pytest.mark.parametrize('preco', [1, 30])
def test_produto_metodo_calcular_preco_com_frete(preco):
	try:
		prod = loja.Produto('Jogo online', preco)
	except Exception:
		raise AssertionError('Erro ao instanciar um Produto')
	assert prod.calcular_preco_com_frete() == preco, "O método calcular_preco_com_frete() deve retornar o preço do Produto"


@pytest.mark.parametrize('atributo', ['_ProdutoFisico__peso'])
def test_cria_produtoFisico(atributo):
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, 1000)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoFisico')
	else:
		mensagens_atributos = {'_ProdutoFisico__peso': 'Não criou o atributo privado peso'}
		assert hasattr(prod, atributo), mensagens_atributos[atributo]


def test_produtoFisico_heranca():
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, 1000)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoFisico')
	assert isinstance(prod, loja.Produto) and isinstance(prod, loja.ProdutoFisico), 'A classe ProdutoFisico deve herdar da classe Produto'


def test_produtoFisico_caracteristicas_herdadas():
	try:
		nome, preco = 'Cadeira', 99
		prod = loja.ProdutoFisico(nome, preco, 1000)
		dict_attrs_classe = vars(loja.ProdutoFisico)
		dict_attrs_obj = vars(prod)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoFisico')
	assert ('_Produto__nome' in dict_attrs_obj) and ('_Produto__preco' in dict_attrs_obj) and ('_ProdutoFisico__nome' not in dict_attrs_obj) and ('_ProdutoFisico__preco' not in dict_attrs_obj), 'A classe ProdutoFisico não deve possuir os atributos privados nome e preco'
	assert ('nome' not in dict_attrs_classe) and ('preco' not in dict_attrs_classe), 'A classe ProdutoFisico deve herdar as properties da classe Produto'
	assert prod.nome == nome and prod.preco == preco, 'As properties herdadas pela classe ProdutoFisico não possuem valores válidos'


@pytest.mark.parametrize('nome,preco,peso', [('Copo',5,100)])
def test_cria_produtoFisico_inicializado_corretamente(nome, preco, peso):
	try:
		prod = loja.ProdutoFisico(nome, preco, peso)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoFisico')
	assert hasattr(prod, "_Produto__nome"), "A classe Produto não possui o atributo privado nome"
	assert hasattr(prod, "_Produto__preco"), "A classe Produto não possui o atributo privado preco"
	assert hasattr(prod, "_ProdutoFisico__peso"), "A classe ProdutoFisico não possui o atributo privado peso"
	assert prod._Produto__nome == nome and prod._Produto__preco == preco and prod._ProdutoFisico__peso == peso, 'A classe ProdutoFisico deve inicializar seus atributos e os atributos da super classe corretamente'


@pytest.mark.parametrize('peso', [1000, 3500])
def test_produtoFisico_property_peso(peso):
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, peso)
		assert prod.peso == peso
	except Exception:
		raise AssertionError('Erro no valor da property peso na classe ProdutoFisico')


@pytest.mark.parametrize('peso', ["", []])
def test_cria_produtoFisico_peso_invalido(peso):
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, peso)
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError para ProdutoFisico criado com peso que não é int')
	else:
		raise AssertionError('ProdutoFisico criado com peso inválido')


@pytest.mark.parametrize('peso', [-1000])
def test_cria_produtoFisico_peso_nao_positivo(peso):
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, peso)
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError para ProdutoFisico criado com peso negativo ou igual a zero')
	else:
		raise AssertionError('ProdutoFisico criado com peso negativo ou igual a zero')


@pytest.mark.parametrize('peso', ["", []])
def test_produtoFisico_setter_peso_invalido(peso):
	try:
		valor_inicial = 100
		prod = loja.ProdutoFisico('Cadeira', 99, valor_inicial)
		prod.preco = peso
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError no setter do peso quando o novo_peso não é int')
	assert hasattr(prod, "_ProdutoFisico__peso"), "A classe ProdutoFisico não possui o atributo privado peso"
	assert prod._ProdutoFisico__peso == valor_inicial, "O atributo privado peso não pode ter o seu valor inicial alterado caso o novo_peso seja inválido"


@pytest.mark.parametrize('peso', [0, -100])
def test_produtoFisico_setter_peso_nao_positivo(peso):
	try:
		valor_inicial = 100
		prod = loja.ProdutoFisico('Cadeira', 99, valor_inicial)
		prod.preco = peso
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError no setter do peso quando o novo_peso é negativo ou igual a zero')
	assert hasattr(prod, "_ProdutoFisico__peso"), "A classe ProdutoFisico não possui o atributo privado peso"
	assert prod._ProdutoFisico__peso == valor_inicial, "O atributo privado peso não pode ter o seu valor inicial alterado caso o novo_peso seja negativo ou igual a zero"


@pytest.mark.parametrize('preco,peso,total', [(100,5000,125), (300,9500,347.5)])
def test_produtoFisico_metodo_calcular_preco_com_frete(preco, peso, total):
	try:
		prod = loja.ProdutoFisico('Cadeira', preco, peso)
	except Exception:
		raise AssertionError('Erro ao instanciar um ProdutoFisico')
	assert prod.calcular_preco_com_frete() == total, "O método calcular_preco_com_frete() não calculou o preço com frete do ProdutoFisico corretamente"


@pytest.mark.parametrize('peso,peso_kg', [(1000,1.0), (9500,9.5)])
def test_produtoFisico_metodo_peso_em_kg(peso, peso_kg):
	try:
		prod = loja.ProdutoFisico('Cadeira', 99, peso)
	except Exception:
		raise AssertionError('Erro ao instanciar um ProdutoFisico')
	assert prod.peso_em_kg() == peso_kg, "O método peso_em_kg() não calculou o peso em kg do ProdutoFisico corretamente"


@pytest.mark.parametrize('atributo', ['_ProdutoEletronico__tensao', '_ProdutoEletronico__tempo_garantia'])
def test_cria_produtoEletronico(atributo):
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, 127, 12)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoEletronico')
	else:
		mensagens_atributos = {'_ProdutoEletronico__tensao': 'Não criou o atributo privado tensao',
		'_ProdutoEletronico__tempo_garantia': 'Não criou o atributo privado tempo_garantia'}
		assert hasattr(prod, atributo), mensagens_atributos[atributo]


def test_produtoEletronico_heranca():
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, 127, 12)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoEletronico')
	assert isinstance(prod, loja.ProdutoFisico) and isinstance(prod, loja.ProdutoEletronico), 'A classe ProdutoEletronico deve herdar da classe ProdutoFisico'


def test_produtoEletronico_caracteristicas_herdadas():
	try:
		nome, preco, peso = 'Geladeira', 4500, 29000
		prod = loja.ProdutoEletronico(nome, preco, peso, 127, 12)
		dict_attrs_classe = vars(loja.ProdutoEletronico)
		dict_attrs_obj = vars(prod)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoEletronico')
	assert ('_Produto__nome' in dict_attrs_obj) and ('_Produto__preco' in dict_attrs_obj) and ('_ProdutoFisico__peso' in dict_attrs_obj) and ('_ProdutoEletronico__nome' not in dict_attrs_obj) and ('_ProdutoEletronico__preco' not in dict_attrs_obj) and ('_ProdutoEletronico__peso' not in dict_attrs_obj), 'A classe ProdutoEletronico não deve possuir os atributos privados nome, preco e peso'
	assert ('nome' not in dict_attrs_classe) and ('preco' not in dict_attrs_classe) and ('peso' not in dict_attrs_classe), 'A classe ProdutoEletronico deve herdar as properties da classe ProdutoFisico'
	assert prod.nome == nome and prod.preco == preco and prod.peso == peso, 'As properties herdadas pela classe ProdutoEletronico não possuem valores válidos'


@pytest.mark.parametrize('nome,preco,peso,tensao,tempo_garantia', [('Cafeteira',300,1500,127,6), ('Geladeira',3500,25000,220,12), ('Televisao',4000,8500,0,24)])
def test_cria_produtoEletronico_inicializado_corretamente(nome, preco, peso, tensao, tempo_garantia):
	try:
		prod = loja.ProdutoEletronico(nome, preco, peso, tensao, tempo_garantia)
	except Exception:
		raise AssertionError('Erro no construtor da classe ProdutoEletronico')
	assert hasattr(prod, "_Produto__nome"), "A classe Produto não possui o atributo privado nome"
	assert hasattr(prod, "_Produto__preco"), "A classe Produto não possui o atributo privado preco"
	assert hasattr(prod, "_ProdutoFisico__peso"), "A classe ProdutoFisico não possui o atributo privado peso"
	assert hasattr(prod, "_ProdutoEletronico__tensao"), "A classe ProdutoEletronico não possui o atributo privado tensao"
	assert hasattr(prod, "_ProdutoEletronico__tempo_garantia"), "A classe ProdutoEletronico não possui o atributo privado tempo_garantia"
	assert prod._Produto__nome == nome and prod._Produto__preco == preco and prod._ProdutoFisico__peso == peso and prod._ProdutoEletronico__tensao == tensao and prod._ProdutoEletronico__tempo_garantia == tempo_garantia, 'A classe ProdutoEletronico deve inicializar seus atributos e os atributos da super classe corretamente'


@pytest.mark.parametrize('meses', [9, 12])
def test_produtoEletronico_property_tempo_garantia(meses):
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, 127, meses)
		assert prod.tempo_garantia == meses
	except Exception:
		raise AssertionError('Erro no valor da property tempo_garantia na classe ProdutoEletronico')


@pytest.mark.parametrize('tensao', [0, 127, 220])
def test_produtoEletronico_property_tensao(tensao):
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, tensao, 12)
		assert prod.tensao == tensao
	except Exception:
		raise AssertionError('Erro no valor da property tensao na classe ProdutoEletronico')


@pytest.mark.parametrize('tensao', ["", []])
def test_cria_produtoEletronico_tensao_tipo_invalido(tensao):
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, tensao, 12)
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError para ProdutoEletronico criado com tensao que não é int')
	else:
		raise AssertionError('ProdutoEletronico criado com tensao com tipo inválido')


@pytest.mark.parametrize('tensao', [-1000, 7, 260])
def test_cria_produtoEletronico_tensao_valor_invalido(tensao):
	try:
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, tensao, 12)
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError para ProdutoEletronico criado com tensao com valor diferente de 0, 127 ou 220')
	else:
		raise AssertionError('ProdutoEletronico criado com tensao com valor inválido')


@pytest.mark.parametrize('tensao', ["", []])
def test_produtoEletronico_setter_tensao_tipo_invalido(tensao):
	try:
		valor_inicial = 127
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, valor_inicial, 12)
		prod.tensao = tensao
	except TypeError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de TypeError no setter da tensao quando nova_tensao não é int')
	assert hasattr(prod, "_ProdutoEletronico__tensao"), "A classe ProdutoEletronico não possui o atributo privado tensao"
	assert prod._ProdutoEletronico__tensao == valor_inicial, "O atributo privado tensao não pode ter o seu valor inicial alterado caso o nova_tensao seja inválida"


@pytest.mark.parametrize('tensao', [-1000, 7, 260])
def test_produtoEletronico_setter_tensao_valor_invalido(tensao):
	try:
		valor_inicial = 127
		prod = loja.ProdutoEletronico('Geladeira', 5000, 35000, valor_inicial, 12)
		prod.tensao = tensao
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError no setter da tensao quando a nova_tensao possui valor diferente de 0, 127 ou 220')
	assert hasattr(prod, "_ProdutoEletronico__tensao"), "A classe ProdutoEletronico não possui o atributo privado tensao"
	assert prod._ProdutoEletronico__tensao == valor_inicial, "O atributo privado tensao não pode ter o seu valor inicial alterado caso a nova_tensao seja diferente de 0, 127 ou 220"


@pytest.mark.parametrize('preco,peso,total', [(100,5000,126.25), (300,9000,348.45)])
def test_produtoEletronico_metodo_calcular_preco_com_frete(preco, peso, total):
	try:
		prod = loja.ProdutoEletronico('Geladeira', preco, peso, 127, 12)
	except Exception:
		raise AssertionError('Erro ao instanciar um ProdutoEletronico')
	assert prod.calcular_preco_com_frete() == total, "O método calcular_preco_com_frete() não calculou o preço com frete do ProdutoEletronico corretamente"


@pytest.mark.parametrize('atributo', ['_Ebook__autor', '_Ebook__numero_paginas'])
def test_cria_ebook(atributo):
	try:
		prod = loja.Ebook('Aprenda Python', 20, 'Joao Silva', 130)
	except Exception:
		raise AssertionError('Erro no construtor da classe Ebook')
	else:
		mensagens_atributos = {'_Ebook__autor': 'Não criou o atributo privado autor',
		'_Ebook__numero_paginas': 'Não criou o atributo privado numero_paginas'}
		assert hasattr(prod, atributo), mensagens_atributos[atributo]


def test_ebook_heranca():
	try:
		prod = loja.Ebook('Aprenda Python', 20, 'Joao Silva', 130)
	except Exception:
		raise AssertionError('Erro no construtor da classe Ebook')
	assert isinstance(prod, loja.Produto) and isinstance(prod, loja.Ebook), 'A classe Ebook deve herdar da classe Produto'


def test_ebook_caracteristicas_herdadas():
	try:
		nome, preco = 'Aprenda Python', 20
		prod = loja.Ebook(nome, preco, 'Joao Silva', 130)
		dict_attrs_classe = vars(loja.Ebook)
		dict_attrs_obj = vars(prod)
	except Exception:
		raise AssertionError('Erro no construtor da classe Ebook')
	assert ('_Produto__nome' in dict_attrs_obj) and ('_Produto__preco' in dict_attrs_obj) and ('_Ebook__nome' not in dict_attrs_obj) and ('_Ebook__preco' not in dict_attrs_obj), 'A classe Ebook não deve possuir os atributos privados nome e preco'
	assert ('nome' not in dict_attrs_classe) and ('preco' not in dict_attrs_classe), 'A classe Ebook deve herdar as properties da classe Produto'
	assert prod.nome == nome and prod.preco == preco, 'As properties herdadas pela classe Ebook não possuem valores válidos'


@pytest.mark.parametrize('nome,preco,autor,numero_paginas', [('Aprendendo Python',30,'Joao Santos',150), ('Learning Java',250,'John da Silva',810)])
def test_cria_ebook_inicializado_corretamente(nome, preco, autor, numero_paginas):
	try:
		prod = loja.Ebook(nome, preco, autor, numero_paginas)
	except Exception:
		raise AssertionError('Erro no construtor da classe Ebook')
	assert hasattr(prod, "_Produto__nome"), "A classe Produto não possui o atributo privado nome"
	assert hasattr(prod, "_Produto__preco"), "A classe Produto não possui o atributo privado preco"
	assert hasattr(prod, "_Ebook__autor"), "A classe Ebook não possui o atributo privado autor"
	assert hasattr(prod, "_Ebook__numero_paginas"), "A classe Ebook não possui o atributo privado numero_paginas"
	assert prod._Produto__nome == nome and prod._Produto__preco == preco and prod._Ebook__autor == autor and prod._Ebook__numero_paginas == numero_paginas, 'A classe Ebook deve inicializar seus atributos e os atributos da super classe corretamente'


@pytest.mark.parametrize('nome,autor', [('Aprendendo Python', 'Joao Santos'), ('Learning Java','John da Silva')])
def test_ebook_property_nome_exibicao(nome, autor):
	try:
		prod = loja.Ebook(nome, 30, autor, 100)
		saida_esperada = '%s (%s)' % (nome, autor)
		temp = prod.nome_exibicao
		temp = re.sub(r'\s+', ' ', temp)
		temp = re.sub(r'[(]\s+', '(', temp)
		temp = re.sub(r'\s+[)]', ')', temp).strip()
		assert temp.upper() == saida_esperada.upper()
	except Exception:
		raise AssertionError('Erro no valor da property nome_exibicao na classe Ebook')


@pytest.mark.parametrize('numero_paginas', [100, 564])
def test_ebook_property_numero_paginas(numero_paginas):
	try:
		prod = loja.Ebook('Aprenda Python', 30, 'Joao da Silva', numero_paginas)
		assert prod.numero_paginas == numero_paginas
	except Exception:
		raise AssertionError('Erro no valor da property numero_paginas na classe Ebook')


@pytest.mark.parametrize('numero_paginas', [0, -1])
def test_cria_ebook_numero_paginas_nao_positivo(numero_paginas):
	try:
		prod = loja.Ebook('Aprenda Python', 30, 'Joao da Silva', numero_paginas)
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError para Ebook criado com numero_paginas negativo ou igual a zero')
	else:
		raise AssertionError('Ebook criado com numero_paginas negativo ou igual a zero')


@pytest.mark.parametrize('numero_paginas', [0, -1])
def test_ebook_setter_numero_paginas_nao_positivo(numero_paginas):
	try:
		valor_inicial = 100
		prod = loja.Ebook('Aprenda Python', 30, 'Joao da Silva', valor_inicial)
		prod.numero_paginas = numero_paginas
	except ValueError:
		pass
	except Exception:
		raise AssertionError('Erro diferente de ValueError no setter do numero_paginas quando o valor não é positivo')
	assert hasattr(prod, "_Ebook__numero_paginas"), "A classe Ebook não possui o atributo privado numero_paginas"
	assert prod._Ebook__numero_paginas == valor_inicial, "O atributo privado numero_paginas não pode ter o seu valor inicial alterado caso o valor seja negativo ou igual a zero"


if __name__ == "__main__":
	pytest.main()

