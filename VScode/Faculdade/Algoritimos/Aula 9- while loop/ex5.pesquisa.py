"""
Uma pesquisa realizada sobre a população de uma determinada região coletou os seguintes
dados, referentes a cada habitante, para serem analisados:
• Idade (em anos)
• Sexo (M - masculino, F - feminino)
A fim de indicar o final da entrada, após a sequência de dados dos habitantes, o usuário entrará com
o valor -1 para a idade, o que deve ser interpretado pelo programa como fim de entrada de dados.
Faça um programa que calcule e mostre:
 a maior idade dentre os habitantes desta pesquisa;
 a menor idade dentre os habitantes desta pesquisa;
 o percentual de indivíduos do sexo feminino com idade entre 18 e 35 anos;
 o percentual de indivíduos (não importando o sexo) com idade maior ou igual a 65 anos.
"""

percentual_feminino = 0
percentual_65 = 0
entreidade_feminino = 0
maior = None
menor = None
maior_65 = 0
i = 1
M = 0
F = 0
total_geral = 0

while True:
    idade = int(input(f"Usuário {i}, insira a sua idade: "))

    if idade >= 65:
            maior_65 += 1

    elif idade == -1:
        print("Encerrando...")
        break

    sexo = input(f"Usuario {i}, insira o seu gênero (M = masculino e F = feminino): ").upper()
    total_geral += 1

    if sexo == "M":
        M += 1

    elif sexo == "F":
        F += 1
        if (18 <= idade <= 35):
            entreidade_feminino += 1
    

    else:
        print("Comando inválido...")
        break

    
    i += 1

        #atualizar maior numero e menor número
    if maior is None or idade > maior:
        maior = idade
    if menor is None or idade < menor:
        menor = idade

#mostrar o maior e menor idade
if maior is not None and menor is not None:
    print(f"maior idade é: {maior}")
    print(f"menor idade é: {menor}")

#calculo de portencial femino com idade entre 18 e 35
if entreidade_feminino > 0:
    percentual_feminino = (entreidade_feminino / F) * 100
    print(f"O percentual femino que possui a idade entre 18 e 35 anos é de: {percentual_feminino:.2f}%")
else:
    print("Nenhum dado informado com relação a isso...")

#porcentagem com relação a pessoas com idade >= 65
if maior_65 > 0:
    percentual_65 = (maior_65 / i) * 100
    print(f"O percentual de pessoas que tem 65 ou mais na idade é: {percentual_65:.2f}%")