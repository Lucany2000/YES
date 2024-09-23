import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from openai import OpenAI


funds = 10000


def getTickers(filePath):
    if filePath.endswith(".csv"):
        df = pd.read_csv(filePath)
    elif filePath.endswith(".xlsx"):
        df = pd.read_excel(filePath, sheet_name=0, engine='openpyxl')
    return df[df.columns[df.columns.get_loc("Symbol ")]].tolist()


tickers = getTickers("List of All Stock Ticker Symbols - Stock Analysis.csv")

def getStockPrices(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1mo")['Close']
    curr = ticker.history(period="1mo")['Close'].iloc[0]
    return {"current": curr, "history": hist}

result_dict = {}

for s in tickers:
    try:
        result_dict[s] = getStockPrices(s)
    except:
        pass


# print(msft.info)