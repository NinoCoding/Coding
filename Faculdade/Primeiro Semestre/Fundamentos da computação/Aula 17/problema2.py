"""
Crie uma função que receba um valor binário no formato de String e a lista de cartas
representando 8bits.
• Utilize uma estrutura de repetição para percorrer cada elemento da string (número binário), para
cada valor, verifique se o mesmo é igual ao bit 1, se for, deve somar o valor da carta de mesma
posição em uma variável auxiliar.
• Repita o processo até acabar todos os dígitos do número binário.
• Ao término da repetição, retorne o valor decimal calculado.
"""

lista = []

def lista_cartas():
    i = 0
    bits = 2 ** (7 - i)
    while i < 8:
        i += 1
        lista.append(bits)
    return lista

def decimal_bin(binario, cartas):
    decimal = 0
    i = 0
    for bits in binario:
        if bits == "1":
            decimal += cartas[i]
    i += 1
    return decimal


def bin_decimal(decimal):
    valor = int(decimal)
    binario = ''
    return binario

cartas = lista_cartas()
print(cartas)
print(decimal_bin('0001011', cartas))


