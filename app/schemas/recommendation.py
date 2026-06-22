from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    ticker:str