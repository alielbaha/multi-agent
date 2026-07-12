from app.graph.state import AgentState
from app.services.llm_client import call_llm

SYSTEM_PROMPT = """You are a bullish equity analyst debating whether to BUY a stock.
You will be given the company's fundamentals, recent news, and the debate so far.
In round 1, make your opening bull case. In later rounds, respond directly to the
bear's last rebuttal. Defend your position and challenge their weakest points.
Be sharp, specific, and cite numbers. Keep your response around 3 to 4 sentences."""

def bull_analyst_node(state:AgentState):
    ticker = state["ticker"]
    fundamentals_summary = state["fundamentals_summary"]
    news_summary = state["news_summary"]
    history = state["debate_history"]

    debate_so_far = "Debate so far :\n" + "\n".join([f"{debator["role"]}: {debator["content"]}" for debator in history])
    round = state["round_number"] +1

    user_prompt = f"Ticker:{ticker}\nRound: {round}\nFundamentals:\n{fundamentals_summary}\nNews:\n{news_summary}\nDebate history:\n{debate_so_far}\n\n Make your bull arguments"

    bull_response = call_llm(SYSTEM_PROMPT, user_prompt)

    return {"round_number": round, 
            "debate_history": history + [{"role": "bull", "round_number": round, "content": bull_response}],
            }