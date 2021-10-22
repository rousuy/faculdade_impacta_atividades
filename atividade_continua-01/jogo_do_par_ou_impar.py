"""
Você gosta de jogos? Silvio gosta! Ainda mais de jogos matemáticos e que precisam de raciocínio lógico.
Como Silvio é muito criativo, criou um jogo para passar o tempo com seus amigos entre os intervalos das aulas.
O jogo é simples, um de seus amigos diz em voz alta um número natural maior ou igual a dois e Silvio deve dizer
rapidamente o número ímpar anterior e o par posterior ao número pronunciado.

Você é um programador que gosta de desafios, afinal todo programador encara desafios o tempo todo, e por isso se
ofereceu para criar um programa para automatizar a resposta de Silvio, recebendo como entrada um número natural maior
ou igual a dois e exibindo o ímpar anterior e o par posterior.

Entrada
Um número natural maior ou igual a dois.

Saída
Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada
e o segundo é o par que sucede o valor dado na entrada.
"""

# Resposta:
num = int(input())
if num >= 2:
    if num % 2 == 0:
        print(f"{num - 1} {num + 2}")
    else:
        print(f"{num -2} {num + 1}")
