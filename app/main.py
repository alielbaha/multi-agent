from fastapi import FastAPI
from app.schemas.recommendation import RecommendationRequest
from app.agents.fundamentals_analyst import fundamentals_analyst_node

app = FastAPI(title="multi agent system")


@app.get("/health")
def health():
    return {"status": "fine"}


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    state = {
        "ticker": request.ticker,
        "fundamentals": None,
        "fundamentals_summary": None,
    }

    state = fundamentals_analyst_node(state)

    return state
