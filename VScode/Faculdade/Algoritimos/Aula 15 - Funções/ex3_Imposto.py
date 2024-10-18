"""
3. Faça um programa, utilizando funções, que retorne o valor de um produto já com o imposto. Deverão ser utilizado dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto
.
Para este exercício crie três funções:
 entrada() - serve para retornar tanto o custo do produto quanto a porcentagem do imposto;
 somaImposto(porc, custo) - recebe o valor da porcentagem do imposto e o custo do produto.
Retorna o novo custo do produto já com o imposto.
 main() - chamada das funções criadas (chama 2 vezes a entrada e 1 vez a função somaImposto)
e depois mostre o custo com o imposto.
"""

def entrada():
    custo = float(input("Digite o custo do produto: "))
    porc = float(input("Digite a porcentagem do imposto: "))
    return custo, porc

def somaImposto(porc, custo):
    return custo + (custo * porc / 100)

def main():
    custo, porc = entrada()
    print("O custo do produto com o imposto é: ", somaImposto(porc, custo))

main()