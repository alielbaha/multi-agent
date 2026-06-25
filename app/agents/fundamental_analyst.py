from app.graph.state import AgentState
from app.retrieval.fundamentals import get_fundamentals
from app.services.llm_client import call_llm

SYSTEM_PROMPT = """You are a fundamental equity analyst. Given a set of
financial metrics for a stock, write a concise 3-4 sentence assessment of
the company's financial health. Be specific about what the numbers indicate
and avoid generic statements."""


def fundamental_analyst_node(state: AgentState):
    ticker = state["ticker"]

    fundamentals = get_fundamentals(ticker)

    user_prompt = f"Ticker:{ticker} \nMetrics:{fundamentals}"
    summary = call_llm(SYSTEM_PROMPT, user_prompt)

    state["fundamentals"] = fundamentals
    state["fundamentals_summary"] = summary

    return state
