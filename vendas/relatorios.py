import pandas as pd

def gerar_relatorios():
    df_vendas = pd.read_csv('vendas/dados/vendas.csv')

    # Vendas por produto
    vendas_por_produto = df_vendas.groupby('Produto vendido')['Quant. de produtos vendidos'].sum().reset_index()  # Correção no groupby
    print("Vendas por Produto:")
    print(vendas_por_produto)

    # Vendas por data
    vendas_por_data = df_vendas.groupby('Data da venda')['Quant. de produtos vendidos'].sum().reset_index()  # Correção no groupby
    print("Vendas por Data:")
    print(vendas_por_data)

    # Produto mais vendido
    produto_mais_vendido = vendas_por_produto.loc[vendas_por_produto['Quant. de produtos vendidos'].idxmax()]
    print("Produto mais vendido:")
    print(produto_mais_vendido)

    # Produto menos vendido
    produto_menos_vendido = vendas_por_produto.loc[vendas_por_produto['Quant. de produtos vendidos'].idxmin()]
    print("Produto menos vendido:")
    print(produto_menos_vendido)
