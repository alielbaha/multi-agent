from typing import TypedDict, Optional


class AgentState(TypedDict):
    ticker: str
    fundamentals: Optional[dict]
    fundamentals_summary: Optional[str]
