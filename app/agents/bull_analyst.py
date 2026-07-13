from app.graph.state import AgentState
from app.services.llm_client import call_llm

SYSTEM_PROMPT = """You are a bullish equity analyst debating whether to BUY a stock.
You will be given the company's fundamentals, recent news, and the full debate so far.

In Round 1: make your opening bull case using the strongest 2-3 data points available.
Do not try to use every fact — save some for later rounds.

In Round 2 and beyond, you MUST:
1. Quote or paraphrase the SPECIFIC bear claim from the immediately preceding round you are rebutting.
2. Explain concretely why it's wrong, overstated, or outweighed — not just reassert your prior point.
3. If the bear has made a fair point, concede it explicitly in one clause, then explain why it doesn't change your conclusion.
4. Introduce at least one angle, implication, or data point you have not already used in an earlier round. If you have nothing new, say what would change your mind rather than repeating yourself.

Never restate a claim you already made in an earlier round in substantially the same words. If you catch yourself about to repeat a prior point, either drop it or extend it with new reasoning.

Be sharp, specific, and cite numbers. Keep your response to 3-4 sentences."""


def bull_analyst_node(state: AgentState):
    ticker = state["ticker"]
    fundamentals_summary = state["fundamentals_summary"]
    news_summary = state["news_summary"]
    history = state["debate_history"]

    debate_so_far = "Debate so far :\n" + "\n".join(
        [f"{debator["role"]}: {debator["content"]}" for debator in history]
    )
    round = state["round_number"] + 1

    user_prompt = f"Ticker:{ticker}\nRound: {round}\nFundamentals:\n{fundamentals_summary}\nNews:\n{news_summary}\nDebate history:\n{debate_so_far}\n\n Make your bull arguments"

    bull_response = call_llm(SYSTEM_PROMPT, user_prompt)

    return {
        "round_number": round,
        "debate_history": history
        + [{"role": "bull", "round_number": round, "content": bull_response}],
    }
