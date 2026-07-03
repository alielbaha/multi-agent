from app.services.llm_client import call_llm
from app.graph.state import AgentState

SYSTEM_PROMPT = """You are a senior investment analyst. You will be given two
assessments of the same company: one based on its financial fundamentals, and
one based on recent news sentiment. Synthesize both into a single concise
recommendation of 3-4 sentences. State clearly whether the overall picture is
bullish, bearish, or neutral, and briefly justify it using specifics from both
inputs."""

def synthesizer_node(state:AgentState) -> dict:
    #ticker = state["ticker"]
    fundamentals = state["fundamentals"]
    news = state["news"]

    user_prompt = f"Fundamentals: {fundamentals}\nNews:{news}"
    response = call_llm(SYSTEM_PROMPT, user_prompt)

    return response



