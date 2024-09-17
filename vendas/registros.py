from datetime import datetime
import pandas as pd
import os

# Função para capturar os dados das vendas
def registro_vendas():
    dados = []
    while True:
        # Captura e valida a data da venda
        while True:
            data_venda = input("Digite a data da venda em formato (DD/MM/AAAA): ")
            try:
                data = datetime.strptime(data_venda, "%d/%m/%Y")  # 'data' é um objeto datetime
                break
            except ValueError:
                print("O formato da data digitado está fora do padrão solicitado. Digite novamente.")
        
        produto_vendido = input("Digite o produto vendido: ")
        quant_produto = int(input("Digite a quantidade de produtos vendidos: "))
        valor_total = float(input("Digite o valor total da venda: "))
        
        # Armazenando os dados em um dicionário
        venda = {
            "Data da venda": data.strftime("%d/%m/%Y"),  # Usa 'data' (objeto datetime) para formatar como string
            "Produto vendido": produto_vendido,
            "Quant. de produtos vendidos": quant_produto,
            "Total": valor_total
        }
        
        # Adicionando o item do dicionário à lista
        dados.append(venda)
        
        # Pergunta ao usuário se deseja registrar mais vendas
        mais_vendas = input("Deseja registrar outra venda? (s/n): ").strip().lower()
        if mais_vendas != 's':
            break
    
    return dados

# Captura os dados de vendas
dados_vendas = registro_vendas()

# Criação do DataFrame para os dados coletados
df_vendas = pd.DataFrame(dados_vendas)

# Verifica se o arquivo CSV já existe
csv_path = 'vendas/dados/vendas.csv'
file_exists = os.path.isfile(csv_path)

# Salvando os dados em um arquivo .csv no modo append ('a')
df_vendas.to_csv(csv_path, mode='a', header=not file_exists, index=False)

print("Dados adicionados ao arquivo vendas.csv com sucesso.")
