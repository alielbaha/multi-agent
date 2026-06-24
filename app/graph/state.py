from typing import TypedDict, Optional


class AgentState(TypedDict):
    ticker: str
    fundementals: Optional[dict]
    fundementals_summary: Optional[dict]
