# 📦 Sistema de Controle de Estoque

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge) ![Badge Python](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=blue&style=for-the-badge)

## 📝 Descrição

Este projeto é um **Sistema de Gerenciamento de Estoque** desenvolvido em **Python 3**. O objetivo foi criar uma aplicação robusta para controlar a entrada e saída de produtos, aplicando conceitos avançados de lógica de programação e persistência de dados.

A principal evolução neste projeto (em comparação a listas simples) foi a implementação de **Dicionários (`dict`)** para busca rápida de itens e o uso de **arquivos JSON** para que os dados não sejam perdidos ao fechar o programa.

## 🚀 Funcionalidades

- **💾 Persistência de Dados:** O sistema salva e carrega o estoque automaticamente usando um arquivo `estoque.json`.
- **🔄 Fluxo Inteligente (UX):**
  - Se tentar adicionar um produto que já existe, o sistema sugere atualizar a quantidade.
  - Se tentar atualizar um produto que não existe, o sistema sugere criá-lo.
- **🛡️ Proteção de Estoque:** Impede que a quantidade de um produto fique negativa ao remover itens.
- **🔢 Validação de Entradas:** Uso de `try/except` para impedir que o sistema quebre se o usuário digitar letras no lugar de números.
- **📋 CRUD Completo:** Adicionar, Visualizar, Atualizar e Deletar produtos.

## 💻 Tecnologias e Conceitos

- **Python 3**
- **Biblioteca JSON:** Para manipulação de arquivos de dados.
- **Biblioteca OS:** Para verificação de existência de arquivos.
- **Estruturas de Dados:** Dicionários (Hash Maps) para performance.
- **Modularização:** Código dividido em funções específicas (`carregar_dados`, `salvar_dados`, `adicionar`, etc.).

## 📂 Estrutura do Projeto

```text
/
├── estoque.json       # Arquivo onde os dados são salvos (gerado automaticamente)
├── main.py            # Código fonte principal do sistema
├── README.md          # Documentação

```

## 🔧 Como Executar

### Pré-requisitos

Você precisa ter o **Python 3.x** instalado.

### Passo a passo

1. Clone o repositório:

```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)

```

2. Execute o arquivo principal:

```bash
python main.py

```

3. O arquivo `estoque.json` será criado automaticamente na primeira execução.

## 🧠 Destaques de Lógica

Um dos desafios superados foi a lógica para impedir estoque negativo:

```python
if estoque[produto] >= quantidade:
    estoque[produto] -= quantidade
    print(f"Estoque atualizado...")
else:
    print(f"Quantidade insuficiente! O estoque atual é {estoque[produto]}.")

```

---

<p align="center">
Desenvolvido para fins de estudo de Lógica de Programação e Estrutura de Dados.
</p>

```

-----

