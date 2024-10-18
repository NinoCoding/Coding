"""Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente.
A tabela de preços do hospital é a seguinte:"""

"""Escreva um programa que leia:
 o número de dias gastos no hospital;
 o tipo de quarto;
 se usou ou não o WIFI (Sim ou Nao);
 se usou ou não a TV a cabo (Sim ou Nao).
Ao final, emita um relatório, como o exemplo, a seguir:
Número de dias no hospital: 5
Tipo de quarto: ..................... Particular
Diárias: .................................. 1800,00
WIFI: ..................................... 3,00
TV a cabo: ............................ 4,00
Total: ………………………….. 1807,00"""

print("Total de gastos")
total = 0

quarto =input("Qual foi o tipo de quarto escolhido(Particular, Semi-Particular, Coletivo)?: ").strip().lower()
dias = int(input("Quantos dias você ficou no hospital?: "))
wifi = input("Usou o wifi?: ").strip().lower()
tv = input("Usou os serviços da TV?: ").strip().lower()

if (quarto == "particular"):
    diaria = dias * 360
elif (quarto == "semi-particular"):
    diaria = dias * 210
elif (quarto == "coletivo"):
    diaria = dias * 185
else:
    print("Tipo invalido! Atribuido o quarto particular")
    diaria = dias * 360
    quarto = "Particular"


if (wifi == "sim") or (wifi == "s"):
    total += 3

if (tv == "sim") or (wifi == "s"):
    total += 4

total += diaria

print(f"""
Número de dias no hospital: {dias}
Tipo de quarto...............{quarto.title()}
Diárias......................{diaria:.2f}
WIFI.........................{'3,00' if wifi == 'sim' else '0,00'}
TV...........................{'4,00' if tv == 'sim' else '0,00'}
Total........................{total:.2f}
""")

