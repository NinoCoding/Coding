""" 
1. Faça um programa, utilizando funções, que receba três números inteiros e positivos, e que forneça a
soma desses três números.
Para este exercício crie três funções:
 entrada() - retorna um número digitado (fazer a verificação se é positivo);
 calculaSoma(a, b, c) - recebe 3 números inteiros e positivos e retorna a soma deles;
 main() - chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a
função para somar) e depois mostre o resultado.
"""

#funcao que realiza a entrada de dados, onde o usuario digita um numero positivo e que sera chamado depois de acordo com a funcao main
def entrada():
    while True: 
        num = int(input())
        if num > 0:
            return num
        else:
            print("Número inválido. Digite um número positivo.")

#funcao que realiza o calculo da somas dos numeros
def calculaSoma(a, b, c):
    return a + b + c

#funcao main que chama as funcoes de uma so vez, como a entrada e a soma
def main():
    a = entrada()
    b = entrada()
    c = entrada()
    soma = calculaSoma(a, b, c)
    print(soma)

main()