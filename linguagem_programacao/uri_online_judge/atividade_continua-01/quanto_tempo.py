"""
"Não tem jeito!", Julius repete para si mesmo que o trânsito da cidade grande é o maior vilão de seus dias, fazendo
com que gaste muito tempo no percurso entre sua casa e o primeiro emprego, entre seu primeiro emprego e o segundo
emprego, e entre seu segundo emprego até o regresso a casa. Pois é, Julius tem dois empregos!

Julius é ótimo na realização de contas, mas como está sempre com pressa, nunca teve tempo para calcular o tempo total
gasto no trânsito, desde o momento que sai de casa até o momento que regressa. Seu relógio é antigo, não possibilitando
cronometrar um percurso, pausar e continuar a cronometragem no próximo, por isso só sabe o tempo gasto entre os
percursos isoladamente, mas não o tempo gasto nos percursos somados. Até ofereceram um novo relógio com desconto para
Julius, para ele respondeu ao vendedor que "não comprar o relógio daria um desconto maior".

Você, como um bom amigo, se ofereceu para criar um programa que recebe como entrada os tempos dos três percursos de
Julius (de casa até o primeiro emprego, do primeiro emprego até o segundo e do segundo até a casa) e exibe o tempo
total consumido.

Não se esqueça que os três tempos serão dados em minutos.

Entrada
Três números inteiros, um por linha, representando os tempos (em minutos) gastos por Julius em seus percursos.

Saída
O tempo total gasto por Julius seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo.
"""
tempo = []
for v in range(3):
    tempo.append(int(input()))

print(f"{sum(tempo)} minutos")
