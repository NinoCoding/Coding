"""
Na TecPy são fabricados painéis de lâmpadas de LED para o natal que funcionam como pisca-pisca. Esses painéis são compostos de N lâmpadas dispostas horizontalmente lado a lado. Além disso, esses painéis tem um comportamento bem definido: logo ao ser
conectado a uma tomada, algumas lâmpadas acendem instantaneamente. Depois disso, a lâmpada mais à esquerda (a primeira), alterna seu estado de ligado para desligado a cada piscada do painel, todas as outras lâmpadas só alternam seu estado se a lâmpada
a sua esquerda apagar. Como você é curioso, você quer saber, dado o número de alternâncias da primeira lâmpada, qual é a configuração final do Painel.


Entrada:
A primeira linha da entrada contém um número inteiro N que especifica a quantidade de casos de teste. Depois haverá N linhas, cada uma contendo uma string P (com no mínimo 1 caractere e no máximo 60) que representa a configuração inicial do painel de
lâmpadas. As lâmpadas inicialmente acesas são representadas pelo caractere 'O' e as apagadas por 'X'. Na mesma linha haverá também um número inteiro C (1 ≤ C ≤ 1018) que representa a quantidade de alternâncias da primeira lâmpada.

Saída:
A saída consiste em uma linha por caso de teste contendo a configuração final do painel após as alternâncias estipuladas para a
primeira lâmpada
"""

#1 - escrever os casos de teste
#2 - fazer a função do programa
#3- escrever a saída e as luzes acesas e apagadas

def testes():
    N = int(input("Digite os casos de testes: "))

    for _ in range(N):
        entrada = input().split()
        C = int(entrada[1])
        P = list(entrada[0])

        
        if C % 2 == 1:
            P[0] = 'X' if P[0] == 'O' else 'O'

        for i in range(1, len(P)):
            if P[i-1] == 'X':  
                P[i] = 'X' if P[i] == 'O' else 'O'


        print("".join(P))


testes()

            
