import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_graficos():
    # Carregar dados do CSV
    df = pd.read_csv('vendas/dados/vendas.csv')

    # Converter a coluna 'Data da venda' para o tipo datetime se ainda não estiver
    df['Data da venda'] = pd.to_datetime(df['Data da venda'], format='%d/%m/%Y')  # Correção na coluna

    # Definir o estilo dos gráficos
    sns.set(style="whitegrid")

    # Gráfico de barras - Vendas por Produto
    plt.figure(figsize=(10, 6))
    vendas_por_produto = df.groupby('Produto vendido')['Total'].sum().reset_index()
    sns.barplot(x='Produto vendido', y='Total', data=vendas_por_produto, palette='Blues_d')
    plt.title('Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Vendas Totais')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('vendas_por_produto.png')
    plt.show()

    # Gráfico de linha - Vendas por Data
    plt.figure(figsize=(10, 6))
    vendas_por_data = df.groupby('Data da venda')['Total'].sum().reset_index()  # Correção na coluna
    sns.lineplot(x='Data da venda', y='Total', data=vendas_por_data, marker='o', color='orange')
    plt.title('Vendas por Data')
    plt.xlabel('Data')
    plt.ylabel('Vendas Totais')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('vendas_por_data.png')
    plt.show()

    # Gráfico de barras - Mais Vendido vs Menos Vendido
    produto_mais_vendido = vendas_por_produto.loc[vendas_por_produto['Total'].idxmax()]
    produto_menos_vendido = vendas_por_produto.loc[vendas_por_produto['Total'].idxmin()]

    df_mais_menos_vendido = pd.DataFrame({
        'Produto': ['Mais Vendido', 'Menos Vendido'],
        'Nome': [produto_mais_vendido['Produto vendido'], produto_menos_vendido['Produto vendido']],
        'Vendas': [produto_mais_vendido['Total'], produto_menos_vendido['Total']]
    })

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Produto', y='Vendas', data=df_mais_menos_vendido, palette='Set2')
    plt.title('Mais Vendido vs Menos Vendido')
    plt.xlabel('Produto')
    plt.ylabel('Vendas Totais')
    plt.tight_layout()
    plt.savefig('mais_menos_vendido.png')
    plt.show()
