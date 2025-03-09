# 5) Escreva um programa que calcule e apresente a soma da seguinte série:
# 1 + 3/2 + 5/3 + 7/4 + ... + 99/50

soma = 0

for i in range(0, 100, 2):
    numerador = 1 + i
    denominador = (i // 2) + 1
    soma += numerador / denominador


print(f"{soma:.2f}")