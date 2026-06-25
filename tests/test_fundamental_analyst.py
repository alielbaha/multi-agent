from unittest.mock import patch
from app.agents.fundamental_analyst import fundamental_analyst_node


@patch("app.agents.fundamental_analyst.call_llm")
@patch("app.agents.fundamental_analyst.get_fundamentals")
def test_fundamental_analyst_node(mock_get_fundamentals, mock_call_llm):
    mock_get_fundamentals.return_value = {
        "pe_ratio": 25.0,
        "market_cap": 2_000_000_000,
        "revenue_growth": 0.12,
        "profit_margins": 0.21,
        "debt_to_equity": 1.5,
    }

    mock_call_llm.return_value = "this company has pretty healthy margins"

    state = {"ticker": "AAPL", "fundamentals": None, "fundamentals_summary": None}

    result = fundamental_analyst_node(state)

    assert result["fundamentals"]["pe_ratio"] == 25.0
    assert result["fundamentals_summary"] == "this company has pretty healthy margins"

    mock_get_fundamentals.assert_called_once_with("AAPL")
