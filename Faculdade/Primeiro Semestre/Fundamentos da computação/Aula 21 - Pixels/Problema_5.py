"""
• Utilizando os pilares do pensamento computacional nos conceitos abordados nesta
aula, faça:
• Um pseudocódigo para gerar uma imagem, utilizando o símbolo * para cor preta e
espaço para cor branca, com base em uma matriz de bits previamente cadastrada
"""

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
         [0, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
         [0, 1, 0, 1, 1, 1, 1, 0, 1, 0], 
         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1], 
         [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], 
         [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], 
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
         [0, 0, 1, 1, 0, 0, 1, 1, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for linha in matriz:
    for elemento in linha:
        if elemento == 0:
            print(" ", end=" ")
        else:
            print("#", end=" ")
    print()
