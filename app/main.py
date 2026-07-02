from fastapi import FastAPI
from app.schemas.recommendation import RecommendationRequest

# from app.agents.fundamentals_analyst import fundamentals_analyst_node
from app.graph.pipeline import graph

app = FastAPI(title="multi agent system")


@app.get("/health")
def health():
    return {"status": "fine"}


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    initial_state = {
        "ticker": request.ticker,
        "fundamentals": None,
        "fundamentals_summary": None,
        "news": None,
        "news_summary": None,
    }

    state = graph.invoke(initial_state)

    return state
