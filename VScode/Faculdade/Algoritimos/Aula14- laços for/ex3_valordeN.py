# Elabore um programa que calcule e apresente o valor de S, dado por:
# 
#         1      2      3           N-1
# S =  ----- + ----- + ----- + ... + ----- + N
#        N      N-1    N-2         2
# 
# Sendo N fornecido pelo usuário.

n = int(input("Informe o valor de N: "))
i = 1
S = 0

while i < n:
    S += i / (n - (i - 1))
    i += 1

S += n
print(S)