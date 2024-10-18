# Imagem representando o cálculo do fatorial de 5: 5! = 5 * 4 * 3 * 2 * 1 = 120

i = 1
fatorial = 1
num = int(input("Insira o número para descobrir o fatorial: "))

while i <= num:
    fatorial *= i
    i += 1

print("5! é igual a: ", fatorial)