"""
2. Faça um programa, utilizando funções, que terá um número inteiro como entrada e a função retornará o caractere "P", se o número for positivo (> 0), "N", se o número for negativo (< 0) e "Zero" se o número for igual a zero.

Para este exercício crie duas funções:
 verifica(a) - recebe o número e retorna "P" (> 0), "N" (< 0) ou "Zero" (igual a 0).
 main() - digita um número, faz a chamada à função verifica e depois mostra o resultado.
"""

def verifica(a):
    if a > 0:
        return "P"
    elif a < 0:
        return "N"
    else:
        return "Zero"
    
def main():
    a = verifica(int(input()))
    print(a)

main()
