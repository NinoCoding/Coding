"""
Desta forma o grupo deve resgatar o projeto 1, fazer ajustes que forem necessários para que ele atenda todos os requisitos solicitados anteriormente (disponível na descrição do Projeto 1) e fazer os seguintes ajustes: 

 

- Modularizar o código: como o objetivo de modularização é organizar o código e praticar reuso, nesta nova versão o projeto deve ter uma função para cada funcionalidade do sistema e um programa principal que faça a chamada devida destas funções. 

- Fazer uso de sequências: para melhor manipulação das informações, algumas variáveis do projeto podem fazer uso do conceito de vetor, utilizando listas para, por exemplo, armazenar o preço do ingresso, os contadores, os acumuladores, entre outros dados. 

- Incluir nova funcionalidade – Controle de Poltronas: ao fazer a compra do ingresso, nesta versão o sistema, no momento da compra, deve fornecer ao usuário o número das poltronas disponíveis e o usuário irá informar o tipo do ingresso e qual a poltrona ele deseja. 

O sistema desta forma deverá controlar as poltronas disponíveis e já vendidas em cada sessão, lembrando que quando não houver mais poltrona disponível, o sistema deve avisar o usuário que aquela sessão não tem mais disponibilidade. 

- Incluir pelo menos mais uma funcionalidade: além da funcionalidade acima, obrigatório, o grupo deve definir uma nova funcionalidade no sistema a sua escolha. 

OBS: 	Não é permitido utilizar estruturas avançadas que não foram tratadas na disciplina Algoritmos e Programação I. Utilize somente os conteúdos abordados nas aulas, ou seja, variáveis, decisão, repetição, funções, sequências e arquivo (opcional). 
"""

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
            input("Pressione Enter para continuar...")

        else:
            print("Opção inválida. Escolha um número entre 1 e 4.")
            input("Pressione Enter para continuar...")
           
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
    
    if escolha in [1, 2, 3]:
        filme_index = escolha - 1
        nota = int(input(f"Qual sua nota para o Filme - {escolha} (0-10): "))
        
        # Armazenar a nota e atualizar contador
        filmes_nota[filme_index].append(nota)
        contadores[filme_index] += 1
        
        # Calcular a média
        media_nota = sum(filmes_nota[filme_index]) / contadores[filme_index]
        print(f"Você deu nota {nota} para o filme {escolha}. Média atual: {media_nota:.2f}")
        input("Pressione Enter para voltar ao menu principal...")
        menu()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

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
assentos_ocupados_filme1_sessao1 = [0, 0, 0]  
assentos_ocupados_filme1_sessao2 = [0, 0, 0]
assentos_ocupados_filme2_sessao1 = [0, 0, 0]
assentos_ocupados_filme2_sessao2 = [0, 0, 0]
assentos_ocupados_filme3_sessao1 = [0, 0, 0]
assentos_ocupados_filme3_sessao2 = [0, 0, 0]

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
        print("Encerrando o dia e exibindo relatório...")
        break
    else:
        print("Opção inválida. Tente novamente.")