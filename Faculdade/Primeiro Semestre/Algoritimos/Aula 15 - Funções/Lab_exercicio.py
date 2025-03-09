"""
A empresa de transporte MGX precisa ter o controle, para cada viagem realizada por um veículo da empresa, da distância total percorrida, do consumo médio de combustível e do valor gasto com o abastecimento. 

O motorista fornece as seguintes informações (nesta ordem) ao final de cada viagem:  a quilometragem inicial, a quilometragem ao final da viagem, a quantidade (em litros) de combustível gasto e o preço do litro do combustível que utilizou. Esses dados são essenciais para o controle financeiro da empresa e para otimizar a eficiência dos veículos.

Você deverá implementar uma função, em python, que receba estes quatro parâmetros, nesta ordem: Km inicial, Km final, quantidade (em litros) de combustível gasto e preço do litro do combustível. A função deve calcular e mostrar:

a distância percorrida;
o consumo médio (com duas casas decimais);
o valor gasto (com duas casas decimais);
"""


"""def main(km_inicial, km_final, quantidade_litros, preco):
#area onde ira realizar os calculos
    distancia = km_final - km_inicial
    combustivel_gasto = distancia / quantidade_litros
    valor_gasto = quantidade_litros * preco

    print(distancia)
    print(f"{combustivel_gasto:.2f}")    
    print(f"{valor_gasto:.2f}")

km_inicial = int(input())
km_final = int(input())
quantidade_litros = int(input())
preco = float(input())

main(km_inicial, km_final, quantidade_litros, preco)"""

"""def main():

    kmi = int(input())
    kmf = int(input())
    ql = int(input())
    preco = float(input())

    distancia = kmf - kmi
    combustivel_gasto = distancia / ql
    valor_gasto = ql * preco

    print(distancia)
    print(f"{combustivel_gasto:.2f}")    
    print(f"{valor_gasto:.2f}")



main()"""

def calcula(kmi, kmf, ql, preco):
    distancia = kmf - kmi
    combustivel_gasto = distancia / ql
    valor_gasto = ql * preco

def main():
   kmi = int(input())
   kmf = int(input())
   ql = int(input())
   preco = float(input())

   calcula(kmi,kmf,ql,preco)

main()