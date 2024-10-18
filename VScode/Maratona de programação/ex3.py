"""
Dado a posição inicial de um cavalo em um tabuleiro de xadrez e a posição destino, deve se dizer se, com exatamente um único movimento, o cavalo consegue alcançar a posição destino. Se isso for possível, o movimento é classificado como válido, caso contrário, o movimento é dito inválido.


Em um tabuleiro de xadrez se utiliza números, de 1 a 8, para especificar a linha do tabuleiro e letras, de 'a' a 'h' para especificar a coluna.

Entrada
A entrada é composta por uma única linha contendo a posição inicial do cavalo e a posição destino, separadas por um espaço em branco. Uma posição no tabuleiro é especificada por um caractere, que representa a coluna, seguido de um número inteiro que representa a linha.

Saída
A saída consiste em uma linha contendo a mensagem "VALIDO" caso o movimento seja um movimento válido de um cavalo no jogo de xadrez ou "INVALIDO" caso contrário.
"""

#passo 1 - imprimir a matriz de xadres de 8x8, onde as linhas representam números, e as colunas representam letras

#passo 2 - na matriz, o usuario devera escolher o local onde o cavalo começa dentro da matriz


#realizar a lista para fazer a matriz 8x8


#entrada do usuario para inserir onde o cavalo vai começar
posicao = input()