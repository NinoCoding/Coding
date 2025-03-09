def imc(peso1, altura1):
    imc = peso1 / altura1**2
    return imc

def mensagem(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

resultado = imc(peso, altura)
print(mensagem(resultado))