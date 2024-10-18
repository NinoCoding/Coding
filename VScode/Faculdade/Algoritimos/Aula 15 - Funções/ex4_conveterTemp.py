# Considere o problema de conversão de temperatura:
# 
# C = (F - 32) / 1.8
# F = C * 1.8 + 32
# 
# Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de:
#
# Fahrenheit para Celsius (para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário
# deve digitar C).
# 
# Para a construção do programa você deve escrever as seguintes funções:
#
# - exibeMsg() - apenas exibe uma mensagem para ao usuário dizendo o que o programa faz e 
#   informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não tem retorno;
# 
# - verificaOpcao() - a função não tem parâmetro de entrada e retorna “F” ou “C” (fazer a validação
#   para que o usuário só digite F ou C);
#
# - verificaIntervalo() - a função não tem parâmetro de entrada e retorna os valores inicial e final
#   do intervalo (fazer a validação para que o valor inicial seja menor que o valor final);
# 
# - exibeFahrenheitToCelsius(inicio, fim) - essa função recebe como entrada o intervalo de 
#   temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida 
#   para Celsius;
# 
# - exibeCelsiusToFahrenheit(inicio, fim) - essa função recebe como entrada o intervalo de 
#   temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
#   para Fahrenheit

def exibeMsg():
    print("Conversão de temperatura!")
    print("Insira F para converter Faheinheit para Celcious")
    print("Ou, digite C para conveter celcious para faheinteit")

def verificarOpcao():
    opcao = input("Digite a opção: ").upper()
    if opcao == "F":
        return "F"
    elif opcao == "C":
        return "C"
    else:
        print("Opção inválida!")
        return verificarOpcao()

def verificaIntervalo():
    inicial = float(input("Digite o valor inicial: "))
    final = float(input("Digite o valor final: "))
    if inicial < final:
        return inicial, final
    else:
        print("O valor inicial deve ser menor que o final")
        return verificaIntervalo()

def exibeFahrenheitToCelsius(inicio, fim):
    print(f"Convertendo Fahrenheit para Celsius de {inicio} a {fim}")
    for i in range(inicio, fim + 1):
        c = (i - 32) / 1.8
        print(f"{i}F = {c}C")

def exibeCelsiusToFahrenheit(inicio, fim):

    print(f"Convertendo Celsius para Fahrenheit de {inicio} a {fim}")
    for i in range(inicio, fim + 1):
        f = i * 1.8 + 32
        print(f"{i}C = {f}F")

exibeMsg()
verificarOpcao()
verificaIntervalo()
exibeFahrenheitToCelsius(1, 100)
exibeCelsiusToFahrenheit(1, 100)