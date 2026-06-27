from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
    ticker: Field(..., min_length=1, examples="AAPL")
