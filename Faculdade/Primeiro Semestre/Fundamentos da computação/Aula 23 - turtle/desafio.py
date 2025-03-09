"""
Elabore um simples jogo de corrida com 5 tartarugas seguindo as definições
abaixo:
• Cada tartaruga deve possuir uma cor diferente
• A velocidade de movimentação de cada tartaruga deve ser aleatória, com valores no intervalo
de 1 a 10 pixels
• O jogo deve solicitar ao usuário uma cor de tartaruga na qual ele deseja apostar
• Defina um ciclo x para executar a corrida, quando a tartaruga tocar a chegada, verifique se o
usuário acertou, exibindo na tela a mensagem “Parabéns! Você acertou.”, caso o usuário tenha
errado o palpite, apresenta na tela a mensagem “Poxa vida! Você errou”.
"""

import turtle
import random

def criar_tartaruga(cor, y):
    tartaruga = turtle.Turtle()
    tartaruga.color(cor)
    tartaruga.shape('turtle')
    tartaruga.penup()  
    tartaruga.goto(-200, y)
    tartaruga.pendown()  
    tartaruga.speed(random.randint(1, 10))  
    return tartaruga

# variavel que cria as tartarugas
tartaruga_vermelha = criar_tartaruga('red', 100)
tartaruga_verde = criar_tartaruga('green', 80)
tartaruga_azul = criar_tartaruga('blue', 60)
tartaruga_amarela = criar_tartaruga('yellow', 40)
tartaruga_roxa = criar_tartaruga('purple', 20)




aposta = input('Qual tartaruga você quer apostar? (red, green, blue, yellow, purple):  ').strip().lower()

while True:
    for tartaruga in [tartaruga_vermelha, tartaruga_verde, tartaruga_azul, tartaruga_amarela, tartaruga_roxa]:
        tartaruga.forward(random.randint(1, 10))

    if tartaruga.xcor() >= 200:
        vencedor = tartaruga.color()[0]
        break
    else:
        continue
    break

if vencedor == aposta:
    print("Parabéns! Você acertou.")
else:
    print("Poxa vida! Você errou")

turtle.done()