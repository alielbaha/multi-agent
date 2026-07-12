from app.graph.state import AgentState
from app.services.llm_client import call_llm


SYSTEM_PROMPT = """You are a bullish equity analyst debating whether to BUY a stock.
You will be given the company's fundamentals, recent news, and the debate so far.
In round 1, make your opening bull case. In later rounds, respond directly to the
bear's last rebuttal — defend your position and challenge their weakest points.
Be sharp, specific, and cite numbers. Keep your response to 3-4 sentences."""

def bear_analyst_node(state:AgentState):
    fundamentals_summary = state['fundamentals_summary']
    news_summary = state["news_summary"]
    history = state["debate_history"]
    round = state["round_number"]
    debate_history = "Debate_so_far:" + "\n".join([f"Role: {debator["role"]}\nContent: {debator["content"]} " for debator in history])
    user_prompt = f"Round: {round}\nFundamentals: \n{fundamentals_summary}\nNews:\n{news_summary}\nDebate history:\n{debate_history}\n\n State your bear rebuttal"
    bear_response = call_llm(SYSTEM_PROMPT, user_prompt)

    return {
        "debate_history": history + [{"role": "bear","round_number":round, "content": bear_response}],
    }