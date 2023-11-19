from src.modules.data_extractor import get_stock_data
from src.settings import config


def process_and_save_data(tickers):
    for ticker in tickers:
        data = get_stock_data(ticker)
        data.to_csv(f"{config.APP_PATH_ASSETS_CSV_FOLDER}/{ticker.lower()}.csv")


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    process_and_save_data(tickers)
