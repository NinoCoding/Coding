# Variáveis do programa
comando1 = 0
contador1 = 0
contador2 = 0
contador3 = 0
cont_nota1 = 0
cont_nota2 = 0
cont_nota3 = 0
media_filme_1 = 0
media_filme_2 = 0
media_filme_3 = 0


# Variáveis para o filme 1
# Sessão 1
assentos1_ocupados1_inteira = 0
assentos1_ocupados1_meia = 0
assentos1_ocupados1_vip = 0
assentos1_ocupados1_total = 0
filme1_assentos1 = 50
preco1_assento1 = 20

# Sessão 2
assentos1_ocupados2_inteira = 0
assentos1_ocupados2_meia = 0
assentos1_ocupados2_vip = 0
assentos1_ocupados2_total = 0
filme1_assentos2 = 50
preco1_assento2 = 20

# Variáveis para o filme 2
# Sessão 1
assentos2_ocupados1_inteira = 0
assentos2_ocupados1_meia = 0
assentos2_ocupados1_vip = 0
assentos2_ocupados1_total = 0
filme2_assentos1 = 40
preco2_assento1 = 15

# Sessão 2
assentos2_ocupados2_inteira = 0
assentos2_ocupados2_meia = 0
assentos2_ocupados2_vip = 0
assentos2_ocupados2_total = 0
filme2_assentos2 = 40
preco2_assento2 = 15

# Variáveis para o filme 3
# Sessão 1
assentos3_ocupados1_inteira = 0
assentos3_ocupados1_meia = 0
assentos3_ocupados1_vip = 0
assentos3_ocupados1_total = 0
filme3_assentos1 = 30
preco3_assento1 = 10

# Sessão 2
assentos3_ocupados2_inteira = 0
assentos3_ocupados2_meia = 0
assentos3_ocupados2_vip = 0
assentos3_ocupados2_total = 0
filme3_assentos2 = 30
preco3_assento2 = 10

# Menu principal
while comando1 != 8:
    comando1 = int(input(
    "-----------------------------------CinemaMack---------------------------------------\n"
    "===================================================================================\n"
    "Olá! Seja-bem vindo à plataforma do CineMack. Digite o número do assunto ao qual queira acessar:\n"
    "1. Comprar ingressos para Filme 1 - Sessão 1\n"
    "2. Comprar ingressos para Filme 1 - Sessão 2\n"
    "3. Comprar ingressos para Filme 2 - Sessão 1\n"
    "4. Comprar ingressos para Filme 2 - Sessão 2\n"
    "5. Comprar ingressos para Filme 3 - Sessão 1\n"
    "6. Comprar ingressos para Filme 3 - Sessão 2\n"
    "7. Avaliar um filme\n"
    "8. Encerrar o dia e exibir o relatório\n"
    "===================================================================================\n"
    "Escolha: "
    ))

    # Lógica para o filme 1, sessão 1
    if comando1 == 1:
        while True:
            assentos_disponiveis = filme1_assentos1 - assentos1_ocupados1_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 1 - Sessão 1: ", assentos_disponiveis)
            tipo_ingresso1_sessao1 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso1_sessao1 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos1_ocupados1_inteira += q
            elif tipo_ingresso1_sessao1 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos1_ocupados1_meia += c
            elif tipo_ingresso1_sessao1 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos1_ocupados1_vip += v
            elif tipo_ingresso1_sessao1 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos1_ocupados1_total = assentos1_ocupados1_meia + assentos1_ocupados1_inteira + assentos1_ocupados1_vip

    # Lógica para o filme 1, sessão 2
    elif comando1 == 2:
        while True:
            assentos_disponiveis = filme1_assentos2 - assentos1_ocupados2_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 1 - Sessão 2: ", assentos_disponiveis)
            tipo_ingresso1_sessao2 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso1_sessao2 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos1_ocupados2_inteira += q
            elif tipo_ingresso1_sessao2 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos1_ocupados2_meia += c
            elif tipo_ingresso1_sessao2 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos1_ocupados2_vip += v
            elif tipo_ingresso1_sessao2 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos1_ocupados2_total = assentos1_ocupados2_meia + assentos1_ocupados2_inteira + assentos1_ocupados2_vip

    # Lógica para o filme 2, sessão 1
    elif comando1 == 3:
        while True:
            assentos_disponiveis = filme2_assentos1 - assentos2_ocupados1_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 2 - Sessão 1: ", assentos_disponiveis)
            tipo_ingresso2_sessao1 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso2_sessao1 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos2_ocupados1_inteira += q
            elif tipo_ingresso2_sessao1 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos2_ocupados1_meia += c
            elif tipo_ingresso2_sessao1 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos2_ocupados1_vip += v
            elif tipo_ingresso2_sessao1 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos2_ocupados1_total = assentos2_ocupados1_meia + assentos2_ocupados1_inteira + assentos2_ocupados1_vip

    # Lógica para o filme 2, sessão 2
    elif comando1 == 4:
        while True:
            assentos_disponiveis = filme2_assentos2 - assentos2_ocupados2_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 2 - Sessão 2: ", assentos_disponiveis)
            tipo_ingresso2_sessao2 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso2_sessao2 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos2_ocupados2_inteira += q
            elif tipo_ingresso2_sessao2 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos2_ocupados2_meia += c
            elif tipo_ingresso2_sessao2 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos2_ocupados2_vip += v
            elif tipo_ingresso2_sessao2 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos2_ocupados2_total = assentos2_ocupados2_meia + assentos2_ocupados2_inteira + assentos2_ocupados2_vip

    # Lógica para o filme 3, sessão 1
    elif comando1 == 5:
        while True:
            assentos_disponiveis = filme3_assentos1 - assentos3_ocupados1_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 3 - Sessão 1: ", assentos_disponiveis)
            tipo_ingresso3_sessao1 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso3_sessao1 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos3_ocupados1_inteira += q
            elif tipo_ingresso3_sessao1 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos3_ocupados1_meia += c
            elif tipo_ingresso3_sessao1 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos3_ocupados1_vip += v
            elif tipo_ingresso3_sessao1 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos3_ocupados1_total = assentos3_ocupados1_meia + assentos3_ocupados1_inteira + assentos3_ocupados1_vip

    # Lógica para o filme 3, sessão 2
    elif comando1 == 6:
        while True:
            assentos_disponiveis = filme3_assentos2 - assentos3_ocupados2_total
            if assentos_disponiveis <= 0:
                print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
                input()
                break
            print("Assentos disponíveis para Filme 3 - Sessão 2: ", assentos_disponiveis)
            tipo_ingresso3_sessao2 = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):"))
   
            if tipo_ingresso3_sessao2 == 1:
                q = int(input("Quantas inteiras serão?: "))
                assentos3_ocupados2_inteira += q
            elif tipo_ingresso3_sessao2 == 2:
                c = int(input("Quantas meias serão?: "))
                assentos3_ocupados2_meia += c
            elif tipo_ingresso3_sessao2 == 3:
                v = int(input("Quantas VIPs serão?: "))
                assentos3_ocupados2_vip += v
            elif tipo_ingresso3_sessao2 == 4:
                print("Voltando ao menu principal...")
                break
           
            assentos3_ocupados2_total = assentos3_ocupados2_meia + assentos3_ocupados2_inteira + assentos3_ocupados2_vip

    # Lógica para avaliação de filme
    elif comando1 == 7:
        filme_avaliacao = int(input("Escolha o filme para avaliar (1, 2 ou 3): "))
        if filme_avaliacao == 1:
            nota1 = int(input(f"Qual sua nota para o filme {filme_avaliacao} (0-10): "))
            print(f"Você deu nota {nota1} para o filme {filme_avaliacao}. Obrigado pela sua avaliação!")
            contador1 += 1
            cont_nota1 += nota1
           
        elif filme_avaliacao == 2:
            nota2 = int(input(f"Qual sua nota para o filme {filme_avaliacao} (0-10): "))
            print(f"Você deu nota {nota2} para o filme {filme_avaliacao}. Obrigado pela sua avaliação!")
            contador2 += 1
            cont_nota2 += nota2
           
        elif filme_avaliacao == 3:
            nota3 = int(input(f"Qual sua nota para o filme {filme_avaliacao} (0-10): "))
            print(f"Você deu nota {nota3} para o filme {filme_avaliacao}. Obrigado pela sua avaliação!")
            contador3 += 1
            cont_nota3 += nota3
           
        else:
            print("Opção de filme inválida.")


    # Relatório final
    elif comando1 == 8:

        if contador1 == 0:
            media_filme_1 = 0
        else:
            media_filme_1 = cont_nota1 / contador1
        if contador2 == 0:
            media_filme_2 = 0
           
        else:
            media_filme_2 = cont_nota2 / contador2
           
        if contador3 == 0:
            media_filme_3 = 0
           
        else:
            media_filme_3 = cont_nota3/contador3
       
        total_inteiro_s1_f1 = assentos1_ocupados1_inteira*20
        total_vip_s1_f1 = assentos1_ocupados1_vip*1.5*20
        total_meia_s1_f1 = assentos1_ocupados1_meia * 10
     
        total_inteiro_s2_f1 = assentos1_ocupados2_inteira * 20
        total_vip_s2_f1 = assentos1_ocupados2_vip*1.2*20
        total_meia_s2_f1 = assentos1_ocupados2_meia * 10

        total_inteiro_s1_f2 = assentos2_ocupados1_inteira * 15
        total_vip_s1_f2 = assentos2_ocupados1_vip * 15 * 1.5
        total_meia_s1_f2 = assentos2_ocupados1_meia * 7.5

        total_inteiro_s2_f2 = assentos2_ocupados2_inteira * 15
        total_vip_s2_f2 = assentos2_ocupados2_vip * 15 * 1.5
        total_meia_s2_f2 = assentos2_ocupados2_meia * 7.5

        total_inteiro_s1_f3 = assentos3_ocupados1_inteira * 10
        total_vip_s1_f3 = assentos3_ocupados1_vip * 10 * 1.5
        total_meia_s1_f3 = assentos3_ocupados1_meia * 5

        total_inteiro_s2_f3 = assentos3_ocupados2_inteira * 10
        total_vip_s2_f3 = assentos3_ocupados2_vip * 10 * 1.5
        total_meia_s2_f3 =  assentos3_ocupados2_meia * 5

        total_1 = assentos1_ocupados1_inteira + assentos1_ocupados1_vip + assentos1_ocupados1_meia + assentos1_ocupados2_inteira + assentos1_ocupados2_vip + assentos1_ocupados2_meia
        total_2 = assentos2_ocupados1_inteira + assentos2_ocupados1_vip + assentos2_ocupados1_meia + assentos2_ocupados2_inteira + assentos2_ocupados2_vip + assentos2_ocupados2_meia
        total_3 = assentos3_ocupados1_inteira + assentos3_ocupados1_vip + assentos3_ocupados1_meia + assentos3_ocupados2_inteira + assentos3_ocupados2_vip + assentos3_ocupados2_meia
        total_ingressos = total_1 + total_2 + total_3

        receita_1 = total_inteiro_s1_f1 +  total_vip_s1_f1 + total_meia_s1_f1 + total_inteiro_s2_f1 + total_vip_s2_f1 + total_meia_s2_f1
        receita_2 = total_inteiro_s1_f2 + total_vip_s1_f2 + total_meia_s1_f2 + total_inteiro_s2_f2 + total_vip_s2_f2 + total_meia_s2_f2
        receita_3 = total_inteiro_s1_f3 + total_vip_s1_f3 + total_meia_s1_f3 + total_inteiro_s2_f3 + total_vip_s2_f3 + total_meia_s2_f3
        receita_total = receita_1 + receita_2 + receita_3

       

        print("\nFilme 1 - Sessão 1:")
        print("Quantidade de Ingressos Vendidos: ")
        print("- Inteira:",assentos1_ocupados1_inteira)
        print("- VIP:",assentos1_ocupados1_vip)
        print("- Meia:",assentos1_ocupados1_meia)
       
        print("Receita por tipo: (Filme 1 Sessão 1:)")
        print("- Inteira:R$",total_inteiro_s1_f1)
        print("- VIP:R$",total_vip_s1_f1)
        print("- Meia:R$",total_meia_s1_f1)

        print("\nFilme 1 - Sessão 2:")
        print("Quantidade de Ingressos Vendidos: ")
        print("- Inteira:",assentos1_ocupados2_inteira)
        print("- VIP:",assentos1_ocupados2_vip)
        print("- Meia:",assentos1_ocupados2_meia)

        print("Receita por tipo: (Filme 1 - Sessão 2):")
        print("- Inteira:R$",total_inteiro_s2_f1)
        print("- VIP:R$",total_vip_s2_f1)
        print("- Meia:R$",total_meia_s2_f1)

        print("\nFilme 2 - Sessão 1: ")
        print("Quantidade de Ingressos Vendidos: ")
        print("- Inteira:",assentos2_ocupados1_inteira)
        print("- VIP:",assentos2_ocupados1_vip)
        print("- Meia:",assentos2_ocupados1_meia)

        print("Receita por tipo: (Filme 2 - Sessão 1):")
        print("- Inteira:R$",total_inteiro_s1_f2)
        print("- VIP:R$",total_vip_s1_f2)
        print("_ Meia:R$",total_meia_s1_f2)

        print("\nFilme 2 - Sessão 2: ")
        print("Quantidade de ingressos vendidos:")
        print("- Inteira:",assentos2_ocupados2_inteira)
        print("- VIP:",assentos2_ocupados2_vip)
        print("- Meia:",assentos2_ocupados2_meia)

        print("Receita por tipo: (Filme 2 - Sessão 2):")
        print("- Inteira:R$",total_inteiro_s2_f2)
        print("- VIP:R$",total_vip_s2_f2)
        print("_ Meia:R$",total_meia_s2_f2)

        print("\nFilme 3 - Sessão 1: ")
        print("Quantidade de ingressos vendidos:")
        print("- Inteira:",assentos3_ocupados1_inteira)
        print("- VIP:",assentos3_ocupados1_vip)
        print("- Meia:",assentos3_ocupados1_meia)

        print("Receita por tipo: (Filme 3 - Sessão 1):")
        print("- Inteira:R$",total_inteiro_s1_f3)
        print("- VIP:R$",total_vip_s1_f3)
        print("_ Meia:R$",total_meia_s1_f3)

        print("\nFilme 3 - Sessão 2: ")
        print("Quantidade de ingressos vendidos:")
        print("- Inteira:",assentos3_ocupados2_inteira)
        print("- VIP:",assentos3_ocupados2_vip)
        print("- Meia:",assentos3_ocupados2_meia)

        print("Receita por tipo: (Filme 3 - Sessão 2):")
        print("- Inteira:R$",total_inteiro_s2_f3)
        print("- VIP:R$",total_vip_s2_f3)
        print("_ Meia:R$",total_meia_s2_f3)

        print("\nMédia de Avaliações: ")
        print("Filme 1: %.2f " %(media_filme_1))
        print("Filme 2: %.2f" %(media_filme_2))
        print("Filme 3: %.2f " %(media_filme_3))
           

        print("\nO total de Ingressos vendidos no dia foi de:",total_ingressos)
        print("\nA receita total do dia foi de: R$",receita_total)

       

        print("\nRelatório de vendas finalizado.\n")
    else:
        print("Opção inválida. Tente novamente.")
