"""
Uma determinada marca de TV apresenta duas linhas - série 100 e série 200.
 A distância ideal entre o sofá e a TV depende do tamanho
 da tela da TV e também da própria série, conforme mostram as tabelas, a seguir.


implemente um programa, em python, onde o cliente digita a distância (float)
 ideal entre o sofá e o TV e, também, a série (inteiro) escolhida, nesta ordem.
O programa deve calcular o tamanho ideal da tela da TV, de acordo com as informações
das tabelas acima. Se o usuário digitar um número de série que não existe,
 deverá aparecer, exatamente, a seguinte mensagem: "Esta série não existe" ."""

distancia = float(input(""))
serie = int(input(""))

if (serie == 100):
    if (distancia <= 1.4):
        print("32")
    elif (distancia >= 1.5) and (distancia <= 2.6):
        print("37")
    else:
        print("42")

elif(serie == 200):
    if (distancia <= 2.8):
        print("42")
    elif (distancia >= 2.9) and (distancia <= 3.6):
        print("50")
    else:
        print("61")

else:
    print("Esta série não existe")