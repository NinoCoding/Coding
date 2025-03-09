# Função que irá converter binário/octal/hexadecimal para decimal
def bin_para_decimal(valor, base):
    decimal = 0
    for i in range(len(valor)):
        # Binário
        if base == 1:
            decimal += int(valor[i]) * 2 ** (len(valor) - 1 - i)

         # Octal
        elif base == 2:  
            decimal += int(valor[i]) * 8 ** (len(valor) - 1 - i)

         # Hexadecimal
        elif base == 3:  
            hex_chars = "0123456789ABCDEF"
            decimal += hex_chars.index(valor[i]) * 16 ** (len(valor) - 1 - i)
    return decimal

# Função que irá converter decimal para binário/octal/hexadecimal
def decimal_para_bin(valor, base): 
    # Binário
    if base == 1:  
        resultado = []
        while valor > 0:
            resultado.append(str(valor % 2))
            valor //= 2
        return ''.join(reversed(resultado))

    # Octal
    elif base == 2:  
        resultado = []
        while valor > 0:
            resultado.append(str(valor % 8))
            valor //= 8
        return ''.join(reversed(resultado))

    # Hexadecimal  
    elif base == 3:  
        resultado = []
        while valor > 0:
            conveter = valor % 16
            resultado.append(str(conveter) if conveter < 10 else chr(conveter + 55))
            valor //= 16
        return ''.join(reversed(resultado))

# Loop do menu principal
while True:
    escolha = int(input("""
[1] - Converter de binário/octal/hexadecimal para decimal
[2] - Converter de decimal para binário/octal/hexadecimal
[3] - Informações do grupo (imprimir TIA + Nome de cada integrante)
[4] - Sair        
Escolha:   
"""))
   
    # Converter de binário/octal/hexadecimal para decimal     
    if escolha == 1:
        base = int(input("Escolha a base para conversão: \n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\nEscolha: "))

        # Converte para maiúsculas para hex
        valor = input("Digite o valor: ").strip().upper() 

        decimal_resultado = bin_para_decimal(valor, base)
        print("O valor convertido para decimal é:", decimal_resultado)

    # Converter de decimal para binário/octal/hexadecimal
    elif escolha == 2:
        valor = int(input("Digite o valor em decimal: "))
        base = int(input("Escolha a base para conversão: \n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\nEscolha: "))
        resultado = decimal_para_bin(valor, base)
        if base == 1:
            print(f"O valor convertido para binário é: {resultado}")
        elif base == 2:
            print(f"O valor convertido para octal é: {resultado}")
        elif base == 3:
            print(f"O valor convertido para hexadecimal é: {resultado}")

    # Informações do grupo
    elif escolha == 3:
        print("Antônio Augusto, 10723954")
        print("Mateus Felipe, 10723904")

    # Sair do loop e encerrar o programa
    elif escolha == 4:
        print("Saindo...")
        break  

    else:
        print("Escolha inválida. Tente novamente.")
