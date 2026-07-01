import yfinance as yf

def _extract_title(item:dict)-> str:
    if "content" in item:
        return item.get("content",{}).get("title")
    return item.get("title") #might see check documention later to remove the if statemnt


def _extract_publisher(item:dict) -> str:
    if "content" in item:
        return item.get("content",{}).get("provider",{}).get("displayName")
    return item.get("publisher")

def get_news(ticker:str, limit = 5) -> list[dict]:
    stock = yf.Ticker(ticker)
    raw_items = stock.news or []

    headlines = []

    for item in raw_items[:limit]:
        title = _extract_title(item)
        if not title:
            continue
        headlines.append({"title" : title, "publisher" : _extract_publisher(item)})
        return headlines
    






