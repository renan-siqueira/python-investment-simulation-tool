# Stock Investment Simulator

---

## Introduction

This project provides tools for simulating stock investments using historical data. It features a Python-based environment for fetching stock data, simulating investments, and visualizing investment outcomes.

## Features

- Data extraction from **Yahoo Finance API**.
- Simulation of stock investments based on historical data.
- Graphical representation of investment performance.
- Ability to process a list of stock tickers from a **JSON** file.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Setting Up a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts with other Python projects or system-wide packages. To set up a virtual environment, navigate to the project's root directory and run:

```bash
python -m venv venv
```

To activate the virtual environment:

- On Windows:
```bash
.\venv\Scripts\activate
```

- On macOS and Linux:
```bash
source venv/bin/activate
```

### Installing Dependencies

With the virtual environment activated, install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Usage

**Before starting to use the project, make sure that the paths within `src/settings/config.py` are created**

### Data Processor

The `data_processor.py` script is used to fetch and save historical stock data. The stock tickers are read from a JSON file named `stocks.json`.

Create a `stocks.json` file in the project root with the following format:

```json
{
    "data": [
        "AAPL",
        "MSFT",
        "GOOGL",
        ...
    ]
}
```

Run the `data_processor.py` script:

```bash
python data_processor.py
```

---

## Investment Simulation

Use `main.py` to simulate investments based on the fetched data.

1. Edit `main.py` to specify the stock ticker, purchase date, and sale date.

2. Run the script:

```bash
python main.py
```

---

## License

This project is open-sourced and available to everyone under the [MIT License](LICENSE).
