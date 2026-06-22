from fastapi import FastAPI
from app.schemas.recommendation import RecommendationRequest
app = FastAPI(title="multi agent system")


@app.get("/health")
def health():
    return {"status": "fine"}


@app.post("/recommend")
def recommand(request: RecommendationRequest):
    return {
        "ticker": request.ticker,
        "signal": "BUY",
    }