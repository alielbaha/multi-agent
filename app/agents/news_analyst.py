from app.graph.state import AgentState
from app.services.llm_client import call_llm
from app.retrieval.news import get_news

SYSTEM_PROMPT = """You are a markets news analyst. Given a list of recent
headlines about a company, write a concise 2-3 sentence assessment of the
overall sentiment and any notable themes. Be specific about what the
headlines suggest and avoid generic statements. If no headlines are
available, say so plainly."""


def news_analyst_node(state: AgentState):
    ticker = state["ticker"]

    news = get_news(ticker)
    headlines = "\n".join(f"{item["title"]}" for item in news) or "nothing was found"
    user_prompt = f"Ticker: {ticker}\nHeadlines:\n{headlines}"

    news_summary = call_llm(SYSTEM_PROMPT, user_prompt)
    state["news"] = news
    state["news_summary"] = news_summary
    return state
