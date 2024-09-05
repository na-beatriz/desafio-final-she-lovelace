#  Desafio Final Iniciativa She Lovelace

Neste repositório você encontra o enunciado do Desafio Final da primeira turma da Iniciativa She Lovelace!

## O Problema

Você foi encarregada de desenvolver um sistema de registro de vendas que permite o armazenamento e a análise de dados de vendas de produtos. Este sistema deve ser capaz de registrar cada venda realizada, armazenar essas informações em um arquivo CSV (banco de dados), e gerar relatórios que ofereçam informações sobre o desempenho das vendas.

## Requisitos do Sistema

1. **Registro de Vendas**: O sistema deve permitir o registro de vendas, capturando informações como data da venda, produto vendido, quantidade e valor total.
2. **Armazenamento de Dados**: As informações das vendas devem ser armazenadas em arquivos CSV para fácil acesso e manipulação futura.
3. **Geração de Relatórios**:
   - Vendas por produto.
   - Vendas por data.
   - Identificação do produto mais vendido.
4. **Visualização Gráfica**: O sistema deve fornecer representações gráficas simples dos dados de vendas para facilitar a visualização dos resultados.

## Estrutura do Projeto

/desafio-final-she-lovelace
│
├── README.md               # Documentação do projeto
├── main.py                 # Arquivo principal para execução do sistema
├── vendas/
│   ├── registro.py         # Script para registrar vendas
│   ├── relatorios.py       # Script para gerar relatórios
│   └── dados/              
│       └── vendas.csv      # Arquivo CSV para armazenar os dados das vendas
├── graficos/
│   └── gerar_graficos.py   # Script para gerar gráficos de vendas
└── requirements.txt        # Dependências do projeto

## Funcionalidades

1. **Registro de Vendas**: Captura informações como data da venda, produto vendido, quantidade e valor total.
2. **Armazenamento de Dados**: Armazena as informações das vendas em um arquivo CSV.
3. **Geração de Relatórios**:
   - Vendas por produto.
   - Vendas por data.
   - Identificação do produto mais vendido e menos vendido.
4. **Visualização Gráfica**:
   - Gráficos de barras para vendas por produto.
   - Gráficos de linha para vendas por data.
   - Comparação entre o produto mais vendido e o menos vendido.

## Como Usar

1. **Instalação**:
   - Clone o repositório:
     ```bash
     git clone https://github.com/SEU-USUARIO/desafio-final-she-lovelace.git
     cd desafio-final-she-lovelace
     ```
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```
2. **Registro de Vendas**:
   - Execute o arquivo `main.py`:
     ```bash
     python main.py
     ```
   - Siga as instruções na interface de linha de comando para registrar novas vendas.

3. **Geração de Relatórios e Gráficos**:
   - Após registrar vendas, você pode gerar relatórios e gráficos executando o comando apropriado na interface de linha de comando.

## Ferramentas Utilizadas

| Ferramenta     | Descrição                                 |
|----------------|-------------------------------------------|
| `Python`       | Linguagem de programação principal        |
| `csv`          | Biblioteca para manipulação de arquivos CSV |
| `pandas`       | Biblioteca para manipulação e análise de dados |
| `matplotlib`   | Biblioteca para visualização de dados     |
| `seaborn`      | Biblioteca para gráficos estatísticos     |

## Requisitos

O arquivo `requirements.txt` inclui as bibliotecas necessárias para executar o projeto. Instale todas as dependências com:

```bash
pip install -r requirements.txt


<h2> Autora </h2>
Feito com ❤️ por Ana Beatriz Almeida 👋🏽 Entre em contato