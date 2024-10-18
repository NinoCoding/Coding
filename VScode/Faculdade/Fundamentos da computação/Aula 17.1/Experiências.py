"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
"""

casos = int(input())
i = 0

coelhos = 0
sapos = 0
ratos = 0


while i < casos:
    entrada = input()
    num, tipo = entrada.split() 
    num = int(num)  
    
    
    if tipo == "c" or tipo == "C":
        coelhos += num
    elif tipo == "r" or tipo == "R":
        ratos += num
    elif tipo == "s" or tipo == "S":
        sapos += num
    
    i += 1  


total_cobaias = coelhos + ratos + sapos

porcentual_coelhos = (coelhos * 100) / total_cobaias if total_cobaias > 0 else 0
porcentual_ratos = (ratos * 100) / total_cobaias if total_cobaias > 0 else 0
porcentual_sapos = (sapos * 100) / total_cobaias if total_cobaias > 0 else 0

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {porcentual_coelhos:.2f} %")
print(f"Percentual de ratos: {porcentual_ratos:.2f} %")
print(f"Percentual de sapos: {porcentual_sapos:.2f} %")