"""
Escreva um programa que leia uma sequência de números inteiros e positivos, encontre e
imprima o maior e o menor número. A entrada de um número negativo indica que a sequência
terminou.
"""

maior = None
menor = None
num = 0
i = 0

#quant = int(input("Quantas sequências de números você deseja colocar?: "))

while True:
    num = int(input("Insira um número: "))

    if num < 0:
        break

    #atualizar maior numero
    if maior is None or num < menor:
        maior = num

    #atualizar menor numero
    if menor is None or num > menor:
        menor = num

#mostrar o maior e menor numero
if maior is not None and menor is not None:
    print(f"maior número é: {maior}")
    print(f"menor número é: {menor}")
else:
    print("nenhum número válido...")