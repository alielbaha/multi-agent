from app.services.llm_client import call_llm
from app.graph.state import AgentState

# from app.agents.fundamentals_analyst import fundamentals_analyst_node
# from app.agents.news_analyst import news_analyst_node

SYSTEM_PROMPT = """you are a senior investment analyst. You will be given two
assessments of the same company: one based on its financial fundamentals, and
one based on recent news sentiment. Synthesize both into a single concise
recommendation of 3 or 4 sentences. State clearly whether the overall picture is
bullish, bearish, or neutral, and briefly justify it using specifics from both
inputs."""


def synthesizer_node(state: AgentState) -> dict:

    ticker = state["ticker"]
    fundamentals_summary = state["fundamentals_summary"]
    news_summary = state["news_summary"]

    user_prompt = (
        f"Ticker: {ticker}\n\n"
        f"Fundamentals assessment:\n{fundamentals_summary}\n\n"
        f"News sentiment assessment:\n{news_summary}"
    )
    recommendation = call_llm(SYSTEM_PROMPT, user_prompt)

    return {"recommendation": recommendation}
