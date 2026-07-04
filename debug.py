from app.graph.pipeline import graph

initial_state = {
    "ticker": "AAPL",
    "fundamentals": None,
    "fundamentals_summary": None,
    "news": None,
    "news_summary": None,
    "recommendation": None,
}

print("--- Starting Graph Execution ---", flush=True)
final_state = graph.invoke(initial_state)
print("--- Graph Execution Finished ---", flush=True)

print("final state keys:", list(final_state.keys()), flush=True)
print("recommendation value:", final_state.get("recommendation"), flush=True)
