import json
from src.modules.data_extractor import get_stock_data
from src.settings import config


def read_tickers_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['data']


def process_and_save_data(tickers):
    for ticker in tickers:
        data = get_stock_data(ticker)
        data.to_csv(f"{config.APP_PATH_ASSETS_CSV_FOLDER}/{ticker.lower()}.csv")


if __name__ == "__main__":
    tickers = read_tickers_from_json(config.APP_PATH_STOCKS_JSON_FILE)
    process_and_save_data(tickers)
