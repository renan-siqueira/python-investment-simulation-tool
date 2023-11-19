import yfinance as yf


def get_stock_data(ticker, start_date, end_date):
    """
    Extrai os dados históricos de ações do Yahoo Finance.

    :param ticker: Símbolo da ação.
    :param start_date: Data de início para os dados históricos.
    :param end_date: Data de término para os dados históricos.
    :return: DataFrame com os dados históricos.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data['Close']  # Retorna apenas os preços de fechamento
