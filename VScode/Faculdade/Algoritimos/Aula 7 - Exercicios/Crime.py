"""Elabore um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são"""

"""O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder Sim a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ela será classificada como "Inocente"."""

n = 0
print("Posso te interrogar?")

tele = input("Você telefonou para a vítima?: ").strip().lower()
local = input("Você esteve no local?: ").strip().lower()
mora = input("Mora perto da vitíma?: ").strip().lower()
devia = input("Devia algo para ela?: ").strip().lower()
trabalho = input("já trabalhou com ela?: ").strip().lower()

if (tele == "sim") or (tele == "s"):
    n += 1
if (local == "sim") or (local == "s"):
    n += 1
if (mora == "sim") or (mora == "s"):
    n += 1
if (devia == "sim") or (devia == "s"):
    n += 1
if (trabalho == "sim") or (trabalho == "s"):
    n += 1
else:
    print("HMMMMMMMMM")

if (n == 2):
    print("Certo, você é apenas um suspeito")
elif (3 <= n <= 4):
    print("Hmmmm, parece que você é um cúmplice do crime")
elif (n == 5):
    print("ASSASSINO!!")
else:
    print("Hmmmmm, inocente para mim")