# Inicializando as variáveis
cartas = [128, 64, 32, 16, 8, 4, 2, 1]
B = 0
D = 0
i = 0

# Solicitando ao usuário que insira o tipo
tipo = input("Insira o tipo de modo (B para B->D e D para D->B): ").title()

# Verificando se o tipo é "B" ou "D"
if tipo == 'B':
    B = input("Insira o número binário: ")
    while i < len(B):  # Loop enquanto i for menor que o comprimento de B
        if B[i] == "1":
            D += cartas[i]  # Soma o valor correspondente da lista 'cartas'
        i += 1
    print(D)  # Imprime o número decimal resultante

elif tipo == 'D':
    D = int(input("Insira o número decimal: "))
    if D > 1:
        while D > 0:
            print(D % 2, end="")  # Imprime o bit correspondente
            D = D // 2
        print()  # Quebra de linha após o fim da impressão dos bits

else:
    print("Tipo inválido")
