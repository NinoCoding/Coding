#Lista das poltronas de cada sessão de filme
poltronas_filmes = {
        #filme 1 - 50 lugares
        1: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10']
        ],
        #filme 2 - 40 lugares
        2: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
        ],
        #filme 3 - 30 lugares
        3: [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
        ]
    }

#função para imprimir as poltronas disponiveis
def poltronas(poltronas_filmes):
    pass

# Função para chamar a função de compra de ingresso
def Sessao_Filme(filme_assentos, assentos_ocupados, preco_assentos):
    assentos_ocupados_total = sum(assentos_ocupados)
   
    while True:
        assentos_disponiveis = filme_assentos - assentos_ocupados_total
        if assentos_disponiveis == 0:
            print("Ingressos esgotados. Pressione Enter para voltar ao menu principal...")
            input()
            break

        print(f"Assentos disponíveis para esta sessão: {assentos_disponiveis}")
        tipo_ingresso_sessao = int(input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar): "))
   
        if tipo_ingresso_sessao == 4:
            print("Voltando ao menu principal...")
            menu()
            break

        if tipo_ingresso_sessao in [1, 2, 3]:
            quantidade = int(input("Quantos ingressos serão?: "))
            
            # Verificação de quantidade solicitada
            if quantidade > assentos_disponiveis:
                print(f"Não há assentos suficientes! Apenas {assentos_disponiveis} assentos restantes.")
                continue
            

            # Atualiza os contadores de acordo com o tipo de ingresso
            assentos_ocupados[tipo_ingresso_sessao - 1] += quantidade
            assentos_ocupados_total += quantidade
            print(f"{quantidade} ingresso(s) do tipo {tipo_ingresso_sessao} comprado(s) com sucesso!")
            input("Pressione Enter para voltar ao menu principal...")

        else:
            print("Opção inválida. Escolha um número entre 1 e 4.")
           
    return assentos_ocupados  # Retorna os assentos ocupados atualizados


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
        "  [8] Encerrar o dia e exibir o relatório\n"
        "                                                            \n"
        "--------------------------------------------------------------\n"
        "           Digite o número da opção desejada:              \n"
        "=============================================================="
    )

# Listas para armazenar os dados de cada filme e de cada sessão
sessoes = [
    {"assentos_totais": 50, "assentos_ocupados": [0, 0, 0], "preco": 20},  
    {"assentos_totais": 50, "assentos_ocupados": [0, 0, 0], "preco": 20},
    {"assentos_totais": 40, "assentos_ocupados": [0, 0, 0], "preco": 15},  
    {"assentos_totais": 40, "assentos_ocupados": [0, 0, 0], "preco": 15},   
    {"assentos_totais": 30, "assentos_ocupados": [0, 0, 0], "preco": 10},   
    {"assentos_totais": 30, "assentos_ocupados": [0, 0, 0], "preco": 10}
]


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

