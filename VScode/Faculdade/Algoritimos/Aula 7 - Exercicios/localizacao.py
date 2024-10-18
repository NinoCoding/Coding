# Entradas do usuário
cliente = input("Qual é o nome do cliente?: ").title()
regiao = input("De qual região você é (Sul = 1, Norte = 2, Leste = 3, Oeste = 4)?: ")
pecas = int(input("Quantas peças foram vendidas?: "))
vendedor = input("Qual seria o nome do vendedor?: ").title()

# Identificar a quantidade de peças pedidas para calcular o frete
if pecas <= 1000:
    # Realizar os cálculos das peças, o custo do frete com relação ao número de peças vendidas
    if regiao == "1":
        frete = pecas * 1.00
    elif regiao == "2":
        frete = pecas * 1.10
    elif regiao == "3":
        frete = pecas * 1.15
    elif regiao == "4":
        frete = pecas * 1.20

        
elif pecas > 1000:
    if regiao == "1":
        frete = pecas * 0.90
    elif regiao == "2":
        frete = pecas * 1.00
    elif regiao == "3":
        frete = pecas * 1.10
    elif regiao == "4":
        frete = pecas * 1.15

# Cálculo do custo total
custo_pecas = 7 * pecas

# Valor total da venda com acréscimo de 50%
valor_total_venda = custo_pecas * 1.5

# Cálculo da comissão do vendedor (6,5% do valor total de venda)
comissao = valor_total_venda * 0.065

# Cálculo do lucro
lucro = valor_total_venda - custo_pecas - comissao

# Exibindo os resultados
print(f"""
========================================
Frete a ser pago: R$ {frete:.2f}
Custo por peça no total: R$ {custo_pecas:.2f}
Comissão do vendedor: R$ {comissao:.2f}
Valor total de venda: R$ {valor_total_venda:.2f}
Lucro: R$ {lucro:.2f}
========================================
""")
