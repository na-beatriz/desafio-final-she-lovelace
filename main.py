from vendas.registros import registro_vendas
from vendas.relatorios import gerar_relatorios
from graficos.gerar_graficos import gerar_graficos

def main():
    while True:
        print("\nSistema de Registros de Vendas e Balanço das Vendas:")
        print("1. Registrar uma nova venda.")
        print("2. Gerar relatórios.")
        print("3. Gerar gráficos.")
        print("4. Sair.")

        try:
            opcao = int(input("Digite o número da opção que deseja (1-4): "))

            if opcao == 1:
                registro_vendas()
            elif opcao == 2:
                gerar_relatorios()
            elif opcao == 3:
                gerar_graficos()
            elif opcao == 4:
                print("O sistema foi encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 4.")

# Verificação se o script está sendo rodado diretamente
if __name__ == "__main__":
    main()
