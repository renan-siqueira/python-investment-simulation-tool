import matplotlib.pyplot as plt
from src.modules.data_extractor import get_stock_data


# Função para simular o investimento
def simulate_investment(data, buy_date, sell_date):
    if buy_date not in data.index or sell_date not in data.index:
        return "As datas de compra ou venda não estão no intervalo de dados."

    buy_price = data.loc[buy_date]  # Ajustado para obter o preço diretamente
    sell_price = data.loc[sell_date]  # Ajustado para obter o preço diretamente
    return_on_investment = (sell_price - buy_price) / buy_price * 100

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data, label='Preço da Ação')  # Ajustado para usar a série de dados
    plt.scatter([buy_date, sell_date], [buy_price, sell_price], color='red')
    plt.title(f'Investimento em Ações: Compra em {buy_date}, Venda em {sell_date}')
    plt.xlabel('Data')
    plt.ylabel('Preço da Ação')
    plt.legend()
    plt.grid(True)
    plt.show()

    return return_on_investment


def main():

    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2020-12-31"
    data = get_stock_data(ticker, start_date, end_date)

    # Testando a função com datas de exemplo
    result = simulate_investment(data, '2020-06-01', '2020-12-01')
    print('Return (%):', result)


if __name__ == "__main__":
    main()
