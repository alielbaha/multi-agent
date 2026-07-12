from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json

from app.schemas.recommendation import RecommendationRequest

# from app.agents.fundamentals_analyst import fundamentals_analyst_node
from app.graph.pipeline import graph

app = FastAPI(title="multi agent system")


@app.get("/health")
def health():
    return {"status": "fine"}


def build_initial_state(ticker: str):
    initial_state = {
        "ticker": ticker,
        "fundamentals": None,
        "fundamentals_summary": None,
        "news": None,
        "news_summary": None,
        "round_number": 0,
        "debate_history": [],
        "verdict": None,
    }
    return initial_state


def stream_events(ticker: str):
    initial_state = build_initial_state(ticker)

    for event in graph.stream(initial_state, stream_mode="updates"):
        for node_name, node_output in event.items():
            payload = json.dumps({"node": node_name, "output": node_output})
            yield f"data: {payload}\n\n"
    yield 'data {"node": "done"}\n\n'


@app.get("/recommend/stream")
def recommend_stream(ticker: str):
    return StreamingResponse(
        stream_events(ticker),
        media_type="text/event-stream",
        headers={"Cache-control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    state = graph.invoke(build_initial_state(request.ticker))
    return state
