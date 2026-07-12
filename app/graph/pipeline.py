from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.agents.fundamentals_analyst import fundamentals_analyst_node
from app.agents.news_analyst import news_analyst_node
# from app.agents.synthesizer import synthesizer_node
from app.agents.bear_analyst import bear_analyst_node
from app.agents.bull_analyst import bull_analyst_node
from app.agents.judge import judge_analyst_node

MAX_ROUNDS = 3

def should_continue(state:AgentState):
    round = state["round_number"]

    if round < MAX_ROUNDS:
        return "continue"
    
    return "end"

builder = StateGraph(AgentState)

builder.add_node("fundamentals_analyst", fundamentals_analyst_node)
builder.add_node("news_analyst", news_analyst_node)
builder.add_node("bull_analyst", bull_analyst_node)
builder.add_node("bear_analyst", bear_analyst_node)
builder.add_node("judge_analyst", judge_analyst_node)


builder.add_edge(START, "fundamentals_analyst")
builder.add_edge(START, "news_analyst")

builder.add_edge("fundamentals_analyst", "bull_analyst")
builder.add_edge("news_analyst", "bull_analyst")

builder.add_edge("bull_analyst", "bear_analyst")

builder.add_conditional_edges("bear_analyst",should_continue, 
                              {
                                  "continue":"bull_analyst",
                                  "end":"judge_analyst",
                                  }
                               )

builder.add_edge("judge_analyst", END)


graph = builder.compile()
