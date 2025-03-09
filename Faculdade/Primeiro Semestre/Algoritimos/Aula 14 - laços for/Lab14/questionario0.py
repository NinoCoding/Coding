# Uma empresa deseja reajustar o salário de seus empregados conforme a seguinte tabela:
#
#      Salário                             Acréscimo
#      superior ou igual a 3.000,00        8%
#      inferior a 3.000,00 mas superior ou igual a 2.000,00   10%
#      inferior a 2.000,00                 12%
#
# Elabore um programa que leia, nesta ordem, a quantidade de empregados e em seguida o salário de cada empregado.
# Calcule e mostre, nesta ordem:
#
# a) para cada empregado, o salário reajustado (conforme tabela);
# b) a quantidade de empregados que receberam reajuste de 10%;
# c) o salário médio (após o reajuste) entre os empregados.
#
# OBS: Lembre-se de que as operações com dinheiro devem conter duas casas decimais para indicar os centavos.
# Formate a saída para adequar o programa a esse contexto (NÃO arredondar antes da formatação).
# Observações importantes para os casos de teste:
# - primeiro digite a quantidade de funcionários;
# - depois digite o salário de cada funcionário;
# - o input NÃO DEVE ter mensagem;
# - a saída deve ser exatamente igual ao(s) caso(s) de teste(s)!
#
# Exemplo:
# Input:
# 3
# 5000.00
# 2800.00
# 1600.00
#
# Result:
# 5400.00
# 3080.00
# 1792.00
# 1
# 3424.00

porcento_10 = 0
soma_salarios = 0.0
media_salarial = 0.0

empregados = int(input())

for i in range(empregados):
    salario = float(input())

    #aumento do salario em 8%
    if salario >= 3000.00:
        aumento = salario * 1.08
        print(f"{aumento:.2f}")
    
    #aumento do salário em 10%
    elif (2000.00 <= salario < 3000.00):
        aumento = salario * 1.10
        porcento_10 += 1
        print(f"{aumento:.2f}")

    else:
        aumento = salario * 1.12
        print(f"{aumento:.2f}")

    soma_salarios += aumento

media_salarial = soma_salarios / empregados


print(porcento_10)
print(f"{media_salarial:.2f}")
