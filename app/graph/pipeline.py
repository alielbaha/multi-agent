from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.agents.fundamentals_analyst import fundamentals_analyst_node
from app.agents.news_analyst import news_analyst_node
from app.agents.synthesizer import synthesizer_node

builder = StateGraph(AgentState)

builder.add_node("fundamentals_analyst", fundamentals_analyst_node)
builder.add_node("news_analyst", news_analyst_node)
builder.add_node("synthesizer", synthesizer_node)

builder.add_edge(START, "fundamentals_analyst")
builder.add_edge(START, "news_analyst")

builder.add_edge("fundamentals_analyst", "synthesizer")
builder.add_edge("news_analyst", "synthesizer")

builder.add_edge("synthesizer", END)


graph = builder.compile()
