preco = float(input("Insira o preço do produto colocado: "))
print("Condição de pagamento: ")
print("1: Á vista em dinheiro ou cheque, recebe 10% de desconto")
print("2: Á vista no cartão de crédito, recebe 5% de desconto")
print("3: em 2 vezes, no preço normal da etiqueta sem juros")
print("4: em 3 vezes, preço normal de etiqueta mais juros de 10%")
print()
codigo = int(input("Insira o código da condição de pagamento: "))

print("Preço original: %.2f" % preco)


if (codigo == 1):
    preco = preco - (preco * 0.10)
    print("o preço atual com desconto é de: %.2f" % preco)

elif (codigo == 2):
    preco = preco - (preco * 0.05)
    print("o valor com desconto é de: %.2f" % preco)

elif (codigo == 3): 
    preco = preco / 2
    print("Você pagará duas parcelas de %.2f" % preco)

elif (codigo == 4):
    preco =preco / 3
    print("Você pagará trẽs parcelas de %.2f" % preco)

else:
    print("código inválido, tente novamente")