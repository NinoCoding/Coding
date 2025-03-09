poltronas_filmes = {
        1: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10']
        ],
        2: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
        ],
        3: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
        ]
    }

#função para imprimir as poltronas disponiveis
def poltrona(escolha, poltronas_filmes, poltronas_ocupadas):
    if escolha in poltronas_filmes:
        print(f"Poltronas Disponíveis para Filme {escolha}: ")
        for fila in poltronas_filmes[escolha]:
            for poltrona in fila:
                status = 'Disponível' if poltrona not in poltronas_ocupadas else 'Ocupado'
                print(f"{poltrona} - {status}")
        print()
    else:
        print("Opção inválida. Tente novamente.")

#função para escolher a poltrona
def escolher_poltrona(poltronas_filmes, poltronas_ocupadas, escolha):
    while True:
        escolha_poltrona = input("Escolha a poltrona (ex: A1, B2, C3, etc.): ").strip()
        if escolha_poltrona in poltronas_filmes[escolha]:
            if escolha_poltrona not in poltronas_ocupadas:
                poltronas_ocupadas.append(escolha_poltrona)

                # Remove da lista de disponíveis
                for fila in poltronas_filmes[escolha]:
                    if escolha_poltrona in fila:
                        fila.remove(escolha_poltrona)
                        break

                print(f"Poltrona {escolha_poltrona} reservada com sucesso!")
                return escolha_poltrona

            else:
                print("Poltrona já ocupada. Escolha outra poltrona.")

        else:
            print("Poltrona inválida. Escolha outra poltrona.")


#função para chamar a função de compra de ingresso
def Sessao_Filme(filme_assentos, poltronas_filmes, poltronas_ocupadas, escolha):
    assentos_disponiveis = len(filme_assentos[escolha]) - len(poltronas_ocupadas)
    while assentos_disponiveis > 0:
        print(f"Assentos disponíveis: {assentos_disponiveis}")
        
        tipo_ingresso_sessao = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar): "))
        if tipo_ingresso_sessao == 4:
            return poltronas_ocupadas

        quantidade = int(input("Quantos ingressos serão?: "))
        if quantidade <= assentos_disponiveis:
            for _ in range(quantidade):
                escolher_poltrona(filme_assentos, poltronas_ocupadas, escolha)
                assentos_disponiveis -= 1
        else:
            print(f"Não há assentos suficientes! Apenas {assentos_disponiveis} assentos restantes.")
    print("Ingressos esgotados para essa sessão.")
    return poltronas_ocupadas

#função para avaliar o filme
def avaliar(nota, contador):
    while True:
        try:
            escolha = int(input(
            "\n====================⭐ Avaliação de Filme⭐ ====================\n"
            "Por favor, escolha o filme que deseja avaliar:\n"
            "  [1] Filme 1\n"
            "  [2] Filme 2\n"
            "  [3] Filme 3\n"
            "  [4] Voltar para o menu\n"
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

            if  escolha == 4:
                print("Voltando ao menu principal...")
                return menu()

            else:
                input("Opção inválida. Por favor, escolha uma opção válida. Pressione enter para continuar.")

        except ValueError:
            input("Opção inválida. Por favor, escolha uma opção válida. Pressione enter para continuar.")

#função para imprimir o relatório
def relatorio():
    precos_base = [20, 15, 10]
    tipos_ingresso = ['Inteira', 'Meia', 'VIP']
    total_ganho = 0

    #impriimindo o relatório de vendas
    print("\n==================== Relatório de Vendas ====================")
    for i, sessao in enumerate(sessoes):
        filme_numero = (i // 2) + 1
        sessao_numero = (i % 2) + 1
        precos_filme = [precos_base[filme_numero - 1], precos_base[filme_numero - 1] / 2, precos_base[filme_numero - 1] * 1.5]
        
        print(f"\nFilme {filme_numero} - Sessão {sessao_numero}:")
        for j in range(len(tipos_ingresso)):
            quantidade = sessao["assentos_ocupados"][j]
            ganho_sessao = quantidade * precos_filme[j]
            total_ganho += ganho_sessao
            print(f"{tipos_ingresso[j]}: {quantidade} ingresso(s) vendidos - Ganho: R${ganho_sessao:.2f}")

    #avaliação de filme
    print("\n====================⭐ Avaliação de Filme⭐ ====================")
    for i, contador in enumerate(contadores):
        if contador > 0:
            media_nota = sum(filmes_nota[i]) / contador
            print(f"Média de avaliações do Filme {i + 1}: {media_nota:.2f}")
        else:
            print(f"Média de avaliações do Filme {i + 1}: Não avaliado")
    print()
    
    #total de ganhos
    print(f"\nTotal ganho: R$ {total_ganho:.2f}")
    print("=============================================================")            

#função para imprimir o menu
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
        "  [8] Encerrar o dia e exibir o relatório\n"
        "                                                            \n"
        "--------------------------------------------------------------\n"
        "           Digite o número da opção desejada:              \n"
        "=============================================================="
    )

# Lista para armazenar as informações do relatorio
filmes_nota = [[] for _ in range(3)]  # Armazenar notas dos 3 filmes
contadores = [0, 0, 0]

# Variáveis
contador1 = contador2 = contador3 = 0
cont_nota1 = cont_nota2 = cont_nota3 = 0

# Lista com os dados das sessões de filmes
sessoes = [
    {"assentos_totais": 50, "assentos_ocupados": [0, 0, 0], "preco": 20},  
    {"assentos_totais": 50, "assentos_ocupados": [0, 0, 0], "preco": 20},
    {"assentos_totais": 40, "assentos_ocupados": [0, 0, 0], "preco": 15},  
    {"assentos_totais": 40, "assentos_ocupados": [0, 0, 0], "preco": 15},   
    {"assentos_totais": 30, "assentos_ocupados": [0, 0, 0], "preco": 10},   
    {"assentos_totais": 30, "assentos_ocupados": [0, 0, 0], "preco": 10}
]

# Chamar e executar o programa
menu()
while True:
    escolha = int(input("Escolha: "))
    # Chamado das funções propostas
    
    match escolha:
        case 1| 2 | 3 | 4 | 5 | 6: 
            indice = escolha - 1
            sessao = sessoes[indice]
            sessao["assentos_ocupados"] = Sessao_Filme(sessao["assentos_totais"], sessao["assentos_ocupados"], sessao["preco"])
        
        case 7:
            avaliar(filmes_nota, contadores)

        case 8:
            relatorio()
            break

        case _:
            print("Opção inválida. Tente novamente.")