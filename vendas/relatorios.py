#3.Geração de Relatórios: O sistema deve gerar relatórios que incluam:
    #Vendas por produto.
    #Vendas por data.
    #Identificação do produto mais vendido.
import pandas as pd

def gerar_relatorios():
    df_vendas = pd.read_csv('vendas/dados/vendas.csv')

    #vendas por produto
    vendas_por_prod = df.groubpy('Produto')['Vendas'].sum().reset_index()
    print("Vendas por Produto:")
    print(vendas_por_produto)

    #vendas por data
    vendas_por_data = df.groupby('Data')['Vendas'].sum().reset_index()
    print("Vendas por Data:")
    print(vendas_por_data)

    #produto mais vendido
    #idxmax serve para encontrar o item como maior número de vendas
    produto_mais_vendido = vendas_por_prod.loc[vendas_por_prod['Vendas'].idxmax()]
    print("Produto mais vendido:")
    print(produto_mais_vendido)

    #produto menos vendido
    produto_menos_vendido = vendas_por_prod.loc[vendas_por_prod['Vendas'].idxmin()]
    print("Produto menos vendido:")
    print(produto_menos_vendido)
