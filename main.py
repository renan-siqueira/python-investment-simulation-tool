import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from src.settings import config

def simulate_investment(data, buy_date, sell_date):
    # Convertendo strings de data para objetos datetime
    buy_date = pd.to_datetime(buy_date)
    sell_date = pd.to_datetime(sell_date)

    # Calculando o intervalo de datas para o gráfico
    start_date = buy_date - timedelta(days=90)
    end_date = sell_date + timedelta(days=90)

    # Limitando os dados ao intervalo de interesse
    plot_data = data.loc[start_date:end_date]

    if buy_date not in plot_data.index or sell_date not in plot_data.index:
        return "Purchase or sale dates are not in the data range."

    buy_price = plot_data.loc[buy_date, 'Close']
    sell_price = plot_data.loc[sell_date, 'Close']
    return_on_investment = (sell_price - buy_price) / buy_price * 100

    plt.figure(figsize=(10, 6))
    plt.plot(plot_data.index, plot_data['Close'], label='Preço da Ação')
    plt.scatter([buy_date, sell_date], [buy_price, sell_price], color='red')
    plt.title(f'Investimento em Ações: Compra em {buy_date.date()}, Venda em {sell_date.date()}')
    plt.xlabel('Data')
    plt.ylabel('Preço da Ação')
    plt.legend()
    plt.grid(True)
    plt.show()

    return return_on_investment


def main():
    ticker = "AAPL"
    data = pd.read_csv(f"{config.APP_PATH_ASSETS_CSV_FOLDER}/{ticker.lower()}.csv")

    data['Date'] = data['Date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d'))
    data.set_index('Date', inplace=True)
    data.index = pd.to_datetime(data.index)

    result = simulate_investment(data, '2020-06-01', '2020-12-01')
    print('Return (%):', result)


if __name__ == "__main__":
    main()