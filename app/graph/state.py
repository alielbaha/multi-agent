from typing import TypedDict, Optional


class AgentState(TypedDict):
    ticker: str
    fundamentals: Optional[dict]
    fundamentals_summary: Optional[str]
    news: Optional[list]
    news_summary: Optional[str]
