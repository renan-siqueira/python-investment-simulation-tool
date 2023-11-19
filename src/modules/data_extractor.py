import yfinance as yf

def get_stock_data(ticker, period="max"):
    """
    Extracts all available historical stock data from Yahoo Finance.

    :param ticker: Symbol of the stock.
    :return: DataFrame with all available historical data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data
