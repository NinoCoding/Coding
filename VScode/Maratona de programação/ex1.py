"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal Secundária da matriz, conforme ilustrado abaixo (área verde)

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

"""
#variaveis gerais
m = []

#pediar ao usuario para fazer a escolha
escolha = input().strip().upper()

#fazendo a matriz 12x12
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    m.append(linha)

# Inicializando variáveis para soma e contagem
soma = 0
contagem = 0

# Cálculo da soma ou média dos elementos abaixo da diagonal secundária
for i in range(1, 12):  
    for j in range(12 - i, 12):  
        soma += m[i][j]
        contagem += 1

# Saída com base na escolha
if escolha == "S":
    print('{:.1f}'.format(soma))

elif escolha == "M":
    media = soma / contagem if contagem > 0 else 0
    print('{:.1f}'.format(media))