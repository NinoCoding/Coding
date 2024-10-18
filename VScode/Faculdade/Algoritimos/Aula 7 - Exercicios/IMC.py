print("indice do IMC")
peso = int(input("insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso/(altura*altura)

print("Seu IMC é: %.2f" % imc)

if (imc < 18.5):
    print("abaixo do peso")

elif (imc >= 18.5) and (imc <= 24.9):
    print("peso normal")

elif (imc >= 25) and (imc <= 29.9):
    print("sobrepeso")

else:
    print("obeso")