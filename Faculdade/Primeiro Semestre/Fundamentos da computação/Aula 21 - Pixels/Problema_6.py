"""
• Utilizando os pilares do pensamento computacional nos conceitos abordados nesta
aula, faça:
• Um pseudocódigo para gerar uma imagem, utilizando o símbolo * para cor preta e
espaço para cor branca, com base em representação numérica previamente
cadastrada
"""

representacao_numerica = [
    [10],
    [4, 2, 4],
    [3, 4, 3],
    [2, 6, 2],
    [1, 2, 1, 2, 1, 2, 1],
    [1, 8, 1],
    [2, 1, 1, 2, 1, 1, 2],
    [1, 1, 6, 1, 1],
    [2, 1, 4, 1, 2],
    [10]
]

for linha in representacao_numerica:
    saida = ""
    branco = True
    for num in linha:
        if branco:
            saida += " " * num
        else:
            saida += "#" * num
        branco = not branco
    print(saida)