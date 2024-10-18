"""
Dado a quantidade de alunos de uma turma e a nota de cada aluno na P1 e na P2, calcular a
média semestral de cada aluno, mostrar uma mensagem "Aprovado direto" para os alunos que
tiveram média maior ou igual a 7 e, ao final, mostrar a média geral da turma.
"""

#variaveis
i = 1
aprovados = 0
reprovados = 0
soma_media = 0
media_geral = 0

alunos = int(input("Insira a quantidade de alunos: "))


while i <= alunos:
        p1 = float(input("Insira a sua nota: "))
        p2 = float(input("Insira a sua segunda nota: "))
        media = (p1 + p2) / 2
        soma_media += media
        i += 1

        if media >= 7:
            print("aprovado, sua média é: ", media)
            aprovados += 1
        
        elif media < 7:
            print("reprovado, sua média é: ", media)
            reprovados += 1

media_geral = soma_media / alunos
print("A média geral da turma é: ", media_geral)
print("Quantidade de alunos aprovados: ", aprovados)
print("Quantidad de alunos reprovados: ", reprovados)


