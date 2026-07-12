from app.services.llm_client import call_llm
from app.graph.state import AgentState

SYSTEM_PROMPT = """ You are an impartial senior investment committee chair.
You have just observed a structured debate between a bull and bear analyst over 3 rounds.
Weigh the quality of each argument across all rounds — who made stronger points,
who had better command of the data, and whose thesis held up under pressure.
Your response must follow this exact format:
VERDICT: [BUY / HOLD / SELL]
RATIONALE: [3 to 4 sentences referencing specific arguments made during the debate] """

def judge_analyst_node(state:AgentState):
    ticker = state["ticker"]
    history = state["debate_history"]
    user_prompt = f"Ticker: {ticker}\nFull debate:\n" + "\n\n".join(
        f"Round: {msg["round_number"]}\n\nRole: {msg["role"]}\n\n{msg["content"]}"
        for msg in history )
    response = call_llm(SYSTEM_PROMPT, user_prompt)
    
    return {"verdict": response}