from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "fine"}


@patch("app.judge.call_llm")
@patch("app.bear_analyst.call_llm")
@patch("app.bull_analyst.call_llm")
@patch("app.news_analyst.call_llm")
@patch("app.news_analyst.get_news")
@patch("app.fundamental_analyst.call_llm")
@patch("app.fundamental_analyst.get_fundamentals")
def test_recommend_end_to_end(
    mock_get_fundamentals,
    mock_call_llm_fundamentals,
    mock_get_news,
    mock_call_llm_news,
    mock_call_llm_bull,
    mock_call_llm_bear,
    mock_call_llm_judge,
):
    mock_get_fundamentals.return_value = {"pe_ratio": 25.0}
    mock_call_llm_fundamentals.return_value = "Solid fundamentals."
    mock_get_news.return_value = []
    mock_call_llm_news.return_value = "Neutral news."
    mock_call_llm_bull.return_value = "Bull argument."
    mock_call_llm_bear.return_value = "Bear argument."
    mock_call_llm_judge.return_value = "VERDICT: HOLD\nRATIONALE: Mixed signals."

    response = client.post("/recommend", json={"ticker": "AAPL"})

    assert response.status_code == 200
    body = response.json()
    assert body["ticker"] == "AAPL"
    assert body["round_number"] == 3
    assert len(body["debate_history"]) == 6  # 3 rounds × 2 speakers
    assert body["debate_history"][0]["role"] == "bull"
    assert body["debate_history"][1]["role"] == "bear"
    assert body["verdict"] == "VERDICT: HOLD\nRATIONALE: Mixed signals."