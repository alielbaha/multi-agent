from typing import TypedDict


class AgentState(TypedDict):
    ticker: str
    fundamentals: dict
    fundamentals_summary: str
    news: list
    news_summary: str
    recommendation: str
    round_number: int
    debate_history: list  # [{"role": "bull/bear", "content": ".."}]
    verdict: str
