# --- 1. Configurações e Dados ---

# Biblioteca para manipulação de arquivos JSON
import json
import os # Vamos usar para verificar se o arquivo existe

def carregar_dados(): #-- Função para carregar os dados do estoque de um arquivo JSON
    if os.path.exists("estoque.json"): # Só tenta ler se o arquivo existir
        try:
            with open("estoque.json", "r") as arquivo:
                dados_carregados = json.load(arquivo)
                return dados_carregados
        except json.JSONDecodeError:
            print("Arquivo de dados vazio ou corrompido.")
            return {}
    else:
        return {} # Se não tiver arquivo, começa com dicionário vazio

estoque = carregar_dados()  #-- Dicionário para armazenar os produtos e suas quantidades

# --- 2. Funções Principais ---
def adicionar_produtos(): #-- Função para adicionar produtos ao estoque
    try:
        produto = input("Digite o nome do produto a ser adicionado: ").upper()
        if produto in estoque: #-- Produto já existe no estoque
            print("Já existe! Indo para atualização...")
            atualizar_estoque() #-- Chama a função de atualização de estoque
        else: #-- Produto não existe no estoque
            quantidade = int(input("Digite a quantidade do produto: "))
            estoque[produto] = quantidade
            print(f"Produto '{produto}' adicionado com quantidade {quantidade}.")
    except ValueError: #-- Tratamento de erro para entrada inválida
        print("Quantidade inválida! Por favor, insira um número inteiro.")

def visualizar_estoque(): #-- Função para visualizar o estoque atual
        if not estoque: #-- Estoque vazio
            print("O estoque está vazio.")
        else: #-- Estoque com produtos
            print("\n--- ESTOQUE ATUAL: ---")
            for produto, quantidade in estoque.items(): #-- Itera sobre os produtos no estoque
                print(f"- {produto}: {quantidade}")
    
def atualizar_estoque(): #-- Função para atualizar a quantidade de um produto no estoque
    try:
        produto = input("\nDigite o nome do produto a ser atualizado: ").upper()

        if produto in estoque: #-- Produto existe no estoque
            print(f"\nQuantidade atual de '{produto}': {estoque[produto]}")
            print("1. Adicionar Quantidade / 2. Remover Quantidade / 3. Voltar")
            while True: #-- Loop para atualizar o estoque do produto
                opcao = input("Escolha uma opção (1-3): ")
                if opcao == '3': ## Voltar
                    break
                elif opcao == '1': ## Adicionar quantidade
                    quantidade = int(input("Digite a quantidade a ser adicionada: "))
                    estoque[produto] += quantidade
                    print(f"Estoque do produto '{produto}' atualizado para {estoque[produto]}.")
                elif opcao == '2': ## Remover quantidade 
                    quantidade = int(input("Digite a quantidade a ser removida: "))
                    if estoque[produto] >= quantidade:
                        estoque[produto] -= quantidade
                        print(f"Estoque do produto '{produto}' atualizado para {estoque[produto]}.")                  
                    else: ## Avisa que a quantidade a ser removida é maior que a disponível no estoque.
                        print(f"Quantidade insuficiente! O estoque atual de '{produto}' é {estoque[produto]}.")                     
        else: #-- Produto não existe no estoque
            print(f"O produto '{produto}' não existe no estoque adicione na (opção 1).")
            adicionar_produtos() #-- Chama a função de adicionar produtos
    except ValueError: #-- Tratamento de erro para entrada inválida
        print("Quantidade inválida! Por favor, insira um número inteiro.")

def excluir_produto(): #-- Função para excluir um produto do estoque
    produto = input("Digite o nome do produto a ser excluído: ").upper()
    if produto in estoque: #-- Produto existe no estoque
        del estoque[produto]
        print(f"Produto '{produto}' foi excluído do estoque.")
    else: #-- Produto não existe no estoque
        print(f"O produto '{produto}' não existe no estoque atual.")

def salvar_dados(): #-- Função para salvar os dados do estoque em um arquivo JSON
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4) # indent=4 deixa o arquivo bonitinho de ler
    print("Dados salvos com sucesso!")

# --- 3. Execução do Programa ---
while True: #-- Loop principal do sistema
    print("\n--- SISTEMA DE CONTROLE DE ESTOQUE ---")
    print("1. Adicionar Produto / 2. Visualizar Estoque / 3. Atualizar Estoque / 4. Excluir Produto / 5. Sair")
    escolha = input("Escolha uma opção (1-5): ")
    if escolha == '5': #-- Sair do sistema
        print("Salvando dados...")
        salvar_dados() #-- Salva os dados antes de sair
        print("Fechando o sistema...")
        break
    elif escolha == '1': #-- Adicionar produto
        adicionar_produtos()
    elif escolha == '2': #-- Visualizar estoque
        visualizar_estoque()
    elif escolha == '3': #-- Atualizar estoque
        atualizar_estoque()
    elif escolha == '4': #-- Excluir produto
        excluir_produto()
    else: #-- Opção inválida
        print("Opção inválida. Tente novamente.")