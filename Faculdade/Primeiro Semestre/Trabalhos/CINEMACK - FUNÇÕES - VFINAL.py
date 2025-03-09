#Integrantes:
#Aline Barbosa Vidal RA: 10721348
#Antonio Augusto Manguetta Feitosa RA: 10723954
#Antonio Costa Satiro de Souza RA: 10723636

# Função para chamar a função de compra de ingresso
def Sessao_Filme(filme_assentos, assentos_ocupados, preco_assentos):
    fileiras = 5
    assentos_por_fileira = filme_assentos // fileiras
    letras_fileiras = ['A', 'B', 'C', 'D', 'E']
    
    # Inicializar a lista de assentos com estado 'L' (livre) para cada tipo de ingresso
    # 0: Inteira, 1: Meia, 2: VIP
    assentos_estado = [['L' for _ in range(assentos_por_fileira)] for _ in range(fileiras)]

    while True:
        assentos_disponiveis = filme_assentos - sum(assentos_ocupados)
        if assentos_disponiveis == 0:
            print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
            input()
            break

        # Exibir o estado atual dos assentos
        print("\nEstado das poltronas (L: Livre, X: Ocupada):")
        for i in range(fileiras):
            fileira = letras_fileiras[i]
            for j in range(assentos_por_fileira):
                if assentos_estado[i][j] == 'L':
                    print(f"[ ] {fileira}{j+1}", end=" ")  # Livre
                else:
                    print(f"[X] {fileira}{j+1}", end=" ")  # Ocupado
            print()

        print()

        tipo_ingresso_sessao = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar): "))
   
        if tipo_ingresso_sessao == 4:
            print("Voltando ao menu principal...")
            break

        if tipo_ingresso_sessao in [1, 2, 3]:
            while True:
                if assentos_disponiveis == 0:
                    print("Não há mais assentos disponíveis.")
                    break
                
                assento_escolhido = input(f"Escolha o número do assento para o ingresso tipo {tipo_ingresso_sessao} (exemplo: A1, B3, 0 para cancelar): ")
                
                if assento_escolhido == "0":
                    break
                
                if len(assento_escolhido) < 2:
                    print(f"Formato inválido. Escolha um assento no formato 'A1', 'B2', etc.")
                    continue

                fileira = assento_escolhido[0].upper()
                numero_assento = int(assento_escolhido[1:])

                if fileira not in letras_fileiras:
                    print("Fileira inválida. Escolha uma letra entre A e E.")
                    continue

                if numero_assento < 1 or numero_assento > assentos_por_fileira:
                    print(f"Assento inválido na fileira {fileira}. Escolha um número entre 1 e {assentos_por_fileira}.")
                    continue

                assento_index = letras_fileiras.index(fileira) * assentos_por_fileira + (numero_assento - 1)
                i = assento_index // assentos_por_fileira
                 # Calcula o índice da fileira
                j = assento_index % assentos_por_fileira
                # Calcula o número do assento na fileira

                if assentos_estado[i][j] != 'L':
                    print(f"Este assento {assento_escolhido} já está ocupado. Escolha outro.")
                else:
                    # Marcar o assento como ocupado de acordo com o tipo de ingresso
                    if tipo_ingresso_sessao == 1:
                        assentos_estado[i][j] = 'X'  # Inteira
                    elif tipo_ingresso_sessao == 2:
                        assentos_estado[i][j] = 'X'  # Meia
                    elif tipo_ingresso_sessao == 3:
                        assentos_estado[i][j] = 'X'  # VIP

                    assentos_ocupados[tipo_ingresso_sessao - 1] += 1  # Incrementa o contador do tipo de ingresso
                    assentos_disponiveis -= 1  # Decrementa os assentos disponíveis
                    print(f"Assento {assento_escolhido} do tipo {tipo_ingresso_sessao} comprado com sucesso!")
                    break

            input("Pressione Enter para voltar ao menu principal...")

        else:
            print("Opção inválida. Escolha um número entre 1 e 4.")
           
    return assentos_ocupados

def avaliar(nota, contador):
    escolha = int(input(
    "\n==================== Avaliação de Filme ====================\n"
    "Por favor, escolha o filme que deseja avaliar:\n"
    "  [1] Filme 1\n"
    "  [2] Filme 2\n"
    "  [3] Filme 3\n"
    "=============================================================\n"
    "Digite o número correspondente ao filme: "
))
    while escolha not in [1,2,3]:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        escolha = int(input(
    "\n==================== Avaliação de Filme ====================\n"
    "Por favor, escolha o filme que deseja avaliar:\n"
    "  [1] Filme 1\n"
    "  [2] Filme 2\n"
    "  [3] Filme 3\n"
    "=============================================================\n"
    "Digite o número correspondente ao filme: "
))
    if escolha in [1, 2, 3]:
        filme_index = escolha - 1
        nota = int(input(f"Qual sua nota para o Filme - {escolha} (0-10): "))
        while nota > 10 or nota < 0:
            print("Opção Inválida. Tente Novamente")
            nota = int(input(f"Qual sua nota para o Filme - {escolha} (0-10): "))
        global filmes_nota, contadores
        
        # Armazenar a nota e atualizar contador
        filmes_nota[filme_index].append(nota)
        contadores[filme_index] += 1
        
        # Calcular a média
        media_nota = sum(filmes_nota[filme_index]) / contadores[filme_index]
        print(f"Você deu nota {nota} para o filme {escolha}. Média atual: {media_nota:.2f}")
        input("Pressione Enter para voltar ao menu principal...")
        menu()
        
def doces_salgados():
    global pipoca_simples, pipoca_grande, chocolate, refrigerante, bala, total_ganho_comida

    while True:
        print(
            "\n======================== 🍬 Doces e Salgados 🍿 ========================\n"
            "                      Bem-vindo à nossa loja!                         \n"
            "------------------------------------------------------------------------\n"
            "Escolha entre nossas deliciosas opções:\n"
            "                                                                        \n"
            "  [1] 🍿 Pipoca Simples - R$ 5,00\n"
            "  [2] 🍿 Pipoca Grande - R$ 10,00\n"
            "  [3] 🍫 Chocolate - R$ 7,00\n"
            "  [4] 🥤 Refrigerante - R$ 6,00\n"
            "  [5] 🍭 Bala de Goma - R$ 3,00\n"
            "  [6] Voltar ao menu principal\n"
            "                                                                        \n"
            "------------------------------------------------------------------------\n"
            "               Digite o número da opção desejada:                      \n"
            "========================================================================"
        )

        opcao = int(input("Escolha: "))
        
        if opcao == 1:
            print("Você escolheu: 🍿 Pipoca Simples - R$ 5,00. Aproveite o filme!")
            pipoca_simples += 1

        elif opcao == 2:
            print("Você escolheu: 🍿 Pipoca Grande - R$ 10,00. Boa escolha!")
            pipoca_grande += 1

        elif opcao == 3:
            print("Você escolheu: 🍫 Chocolate - R$ 7,00. Uma delícia!")
            chocolate += 1

        elif opcao == 4:
            print("Você escolheu: 🥤 Refrigerante - R$ 6,00. Refrescante!")
            refrigerante += 1

        elif opcao == 5:
            print("Você escolheu: 🍭 Bala de Goma - R$ 3,00. Docinho especial!")
            bala += 1

        elif opcao == 6:
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


        total_ganho_comida = (pipoca_simples * 5 + pipoca_grande * 10 + chocolate * 7 + refrigerante * 6 + bala * 3)
        input("Pressione Enter para continuar...")
    menu()

def relatorio():
    global assentos_ocupados_filme1_sessao1, assentos_ocupados_filme1_sessao2
    global assentos_ocupados_filme2_sessao1, assentos_ocupados_filme2_sessao2
    global assentos_ocupados_filme3_sessao1, assentos_ocupados_filme3_sessao2

    # Preços base para cada filme
    precos_base = [20, 15, 10]
    
    # Informações sobre os ingressos vendidos
    tipos_ingresso = ['Inteira', 'Meia', 'VIP']
    
    # Preços dos ingressos
    precos_filme1 = [precos_base[0], precos_base[0] / 2, precos_base[0] * 1.5]
    precos_filme2 = [precos_base[1], precos_base[1] / 2, precos_base[1] * 1.5]
    precos_filme3 = [precos_base[2], precos_base[2] / 2, precos_base[2] * 1.5]
    total_ganho = 0

    # Exibir os assentos ocupados e calcular total ganho
    print("\n==================== Relatório de Vendas ====================")

    # Dinheiro total ganho de doces e bebidas
    print("\nDinheiro da lanchonete:")
    print("Quantidade de pipoca simples comprada(s): ", pipoca_simples)
    print("Quantidade de pipoca grande comprada(s): ", pipoca_grande)
    print("Quantidade de chococate(s) comprada(s): ", chocolate)
    print("Quantidade de refrigerante(s) comprada(s): : ", refrigerante)
    print("Quantidade de bala(s) comprada(s): ", bala)
    print(f"Doces e Bebidas: R${total_ganho_comida:.2f}")
    

    # Sessões do Filme 1
    print("\nFilme 1 - Sessão 1:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme1_sessao1[j]
        ganho_sessao = quantidade * precos_filme1[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    print("\nFilme 1 - Sessão 2:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme1_sessao2[j]
        ganho_sessao = quantidade * precos_filme1[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    # Sessões do Filme 2
    print("\nFilme 2 - Sessão 1:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme2_sessao1[j]
        ganho_sessao = quantidade * precos_filme2[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    print("\nFilme 2 - Sessão 2:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme2_sessao2[j]
        ganho_sessao = quantidade * precos_filme2[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    # Sessões do Filme 3
    print("\nFilme 3 - Sessão 1:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme3_sessao1[j]
        ganho_sessao = quantidade * precos_filme3[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    print("\nFilme 3 - Sessão 2:")
    for j in range(len(tipos_ingresso)):
        quantidade = assentos_ocupados_filme3_sessao2[j]
        ganho_sessao = quantidade * precos_filme3[j]
        total_ganho += ganho_sessao
        print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    total_ganho += total_ganho_comida

    # Exibir total ganho
    print(f"\nTotal ganho: R$ {total_ganho:.2f}")


   # Para o Filme 1
    if contadores[0] > 0:
       media_nota_1 = sum(filmes_nota[0]) / contadores[0]
       print(f"Média de avaliações do Filme 1: {media_nota_1:.2f}")
    else:
        print("Média de avaliações do Filme 1: Não avaliado")
    # Para o Filme 2
    if contadores[1] > 0:
        media_nota_2 = sum(filmes_nota[1]) / contadores[1]
        print(f"Média de avaliações do Filme 2: {media_nota_2:.2f}")
    else:
        print("Média de avaliações do Filme 2: Não avaliado")

    # Para o Filme 3
    if contadores[2] > 0:
        media_nota_3 = sum(filmes_nota[2]) / contadores[2]
        print(f"Média de avaliações do Filme 3: {media_nota_3:.2f}")
    else:
        print("Média de avaliações do Filme 3: Não avaliado")


    print("=============================================================")            


# Menu do arquivo
def menu():
    print(
        "======================== CinemaMack ========================\n"
        "                🎬 Bem-vindo à plataforma! 🎬                \n"
        "--------------------------------------------------------------\n"
        "Escolha uma das opções abaixo:\n"
        "                                                            \n"
        "  [1] Comprar ingressos para Filme 1 - Sessão 1\n"
        "  [2] Comprar ingressos para Filme 1 - Sessão 2\n"
        "  [3] Comprar ingressos para Filme 2 - Sessão 1\n"
        "  [4] Comprar ingressos para Filme 2 - Sessão 2\n"
        "  [5] Comprar ingressos para Filme 3 - Sessão 1\n"
        "  [6] Comprar ingressos para Filme 3 - Sessão 2\n"
        "  [7] Avaliar um filme\n"
        "  [8] Comprar doces e salgados\n"
        "  [9] Encerrar o dia e exibir o relatório\n"
        "                                                            \n"
        "--------------------------------------------------------------\n"
        "           Digite o número da opção desejada:              \n"
        "=============================================================="
    )

# Listas para armazenar os dados de cada filme e de cada sessão
assentos_ocupados_filme1_sessao1 = [0, 0, 0]  
assentos_ocupados_filme1_sessao2 = [0, 0, 0]
assentos_ocupados_filme2_sessao1 = [0, 0, 0]
assentos_ocupados_filme2_sessao2 = [0, 0, 0]
assentos_ocupados_filme3_sessao1 = [0, 0, 0]
assentos_ocupados_filme3_sessao2 = [0, 0, 0]

#variaveis dos doces e salgados
pipoca_simples = 0
pipoca_grande = 0
chocolate = 0
refrigerante = 0
bala = 0
total_ganho_comida = 0


# Lista para armazenar as informações do relatorio
filmes_nota = [[] for _ in range(3)]  # Armazenar notas dos 3 filmes
contadores = [0, 0, 0]

# Variáveis
contador1 = contador2 = contador3 = 0
cont_nota1 = cont_nota2 = cont_nota3 = 0

# Chamar e executar o programa
menu()
while True:
    # Chamado das funções propostas
    escolha = int(input("Escolha: "))
    if escolha == 1:
        assentos_ocupados_filme1_sessao1 = Sessao_Filme(50, assentos_ocupados_filme1_sessao1, 20)

    elif escolha == 2:
        assentos_ocupados_filme1_sessao2 = Sessao_Filme(50, assentos_ocupados_filme1_sessao2, 20)

    elif escolha == 3:
        assentos_ocupados_filme2_sessao1 = Sessao_Filme(40, assentos_ocupados_filme2_sessao1, 15)

    elif escolha == 4:
        assentos_ocupados_filme2_sessao2 = Sessao_Filme(40, assentos_ocupados_filme2_sessao2, 15)

    elif escolha == 5:
        assentos_ocupados_filme3_sessao1 = Sessao_Filme(30, assentos_ocupados_filme3_sessao1, 10)

    elif escolha == 6:
        assentos_ocupados_filme3_sessao2 = Sessao_Filme(30, assentos_ocupados_filme3_sessao2, 10)

    elif escolha == 7:
        avaliar(filmes_nota, contadores)

    elif escolha == 8:
        doces_salgados()
            
    elif escolha == 9:
        print("Encerrando o dia e Exibindo o Relatório...")
        relatorio()
        break
    else:
        print("Opção inválida. Tente novamente.")

