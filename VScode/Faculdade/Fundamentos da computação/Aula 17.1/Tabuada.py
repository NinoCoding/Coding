"""
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N
Entrada

A entrada contém um valor inteiro N (2 < N < 1000).
Saída

Imprima a tabuada de N, conforme o exemplo fornecido.
"""

num = int(input())


if 2 < num < 1000:
    i = 1
    while i <= 10: 
        tabuada = num * i
        print(f"{i} x {num} = {tabuada}")
        i += 1

else:
    print("Invalído")