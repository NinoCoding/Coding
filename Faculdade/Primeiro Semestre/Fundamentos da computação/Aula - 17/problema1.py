def lista():
    i = 0
    bins = []
    while i < 8:
        potencia = 2 ** i
        bins.append(potencia)
        i += 1
    return bins

def lista_reversa():
    i = 0
    bits = []
    while i < 8:
        reversa = 2 ** (7 - i)
        i += 1
        bits.append(reversa)
    return bits

def bin_decimal(cartas, valor_bin):
    decimal = 0
    for i in range(len(valor_bin)):
        if valor_bin[i] == '1':  
            decimal += cartas[i]  
    return decimal

def decima_para_binario(decimal):
    if decimal == 0:
        return '0'
    
    binario = ''
    while decimal > 0:
        resto = decimal % 2  
        binario = str(resto) + binario  
        decimal = decimal // 2  
    
    return binario


valor_bin = '01101101'
cartas = [128, 64, 32, 16, 8, 4, 2, 1]
resultado = bin_decimal(cartas, valor_bin)

decimal = 16
binario = decima_para_binario(decimal)

print(lista())           
print(lista_reversa())    
print(resultado)          
print(binario)            
