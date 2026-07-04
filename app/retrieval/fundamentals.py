import yfinance as yf


def get_fundamentals(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "pe_ratio": info.get("trailingPE"),
        "market_cap": info.get("marketCap"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_margins": info.get("profitMargins"),
        "debt_to_equity": info.get("debtToEquity"),
    }
