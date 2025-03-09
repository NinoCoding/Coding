"""Crie uma função que seja capaz de inicializar uma lista com 8 bits em potência de 2, após finalizar
a inicialização, retorne a lista criada.
• Utilize estrutura de repetição para resolver este problema.
• A função não recebe nenhum parâmetro de entrada.
• A lista deve ser gerada no seguinte formato (valores decrescentes):
[128, 64, 32, 16, 8, 4, 2, 1]"""

lista = []

def potencia():
    i = 0
    while i < 8:
        bits = 2 ** (7 - i)
        i += 1
        lista.append(bits)
    return lista

potencia()
print(lista)
