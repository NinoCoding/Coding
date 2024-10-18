# 6) A conversão de graus Fahrenheit para Celsius é obtida pela fórmula: C = (5/9) * (F - 32).
# Escreva um programa que calcule e apresente uma tabela de graus Celsius em função de graus Fahrenheit que variem de 50 a 150, de 1 em 1.

print(f"{'Fahrenheit':<12} {'Celsius':<12}")

for F in range(50, 151, 1):
    c = (5/9) * (F - 32)
    print(f"{F:<12} {c:.2f}")