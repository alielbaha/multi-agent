# Multi-Agent Financial Analysis System

[![CI](https://img.shields.io/badge/CI-Passing-brightgreen?logo=githubactions&logoColor=white)](https://github.com/alielbaha/multi-agent/actions)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A multi-agent AI system for real-time stock analysis. A fundamentals analyst and a news analyst research a ticker in parallel, then a bull and bear analyst debate the stock over several rounds, and an impartial judge agent weighs the debate to issue a final BUY / HOLD / SELL verdict. Built with LangGraph, FastAPI, and Groq LLMs.

## Features

- **Parallel Research:** Simultaneous fundamentals and news gathering via LangGraph's fan-out pattern.
- **Bull vs. Bear Debate:** A bull analyst and a bear analyst argue opposing sides of the investment case over multiple rounds, each responding directly to the other's last point.
- **Judge Verdict:** An impartial judge agent reviews the full debate transcript and issues a final `VERDICT` (BUY / HOLD / SELL) with a rationale grounded in the arguments made.
- **Real-Time Data:** Live stock metrics and headlines fetched via `yfinance`.
- **LLM-Powered:** Every agent (fundamentals, news, bull, bear, judge) is powered by the Groq API.
- **Streaming Support:** Watch the debate unfold live via a Server-Sent Events endpoint, or get the full result in one call.
- **Production-Ready:** FastAPI backend with Pydantic validation, Docker support, and automated CI/CD (`ruff` + `black`).

## Quick Start

### 1. Installation
```bash
git clone https://github.com/alielbaha/multi-agent.git
cd multi-agent
pip install -r requirements.txt
```

### 2. Configuration
Create `app/.env` and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Server
```bash
uvicorn app.main:app --reload
```

## API Usage

**Health Check**
```bash
curl http://localhost:8000/health
```

**Analyze a Stock**
```bash
curl -X POST http://localhost:8000/recommend \
     -H "Content-Type: application/json" \
     -d '{"ticker": "AAPL"}'
```

Returns the full final state, including the fundamentals/news summaries, the complete bull/bear debate history, and the judge's verdict.

**Stream the Debate Live**
```bash
curl "http://localhost:8000/recommend/stream?ticker=AAPL"
```

Streams each agent's output as a Server-Sent Events (SSE) feed as it completes, so you can watch the research and debate unfold in real time instead of waiting for the full pipeline to finish.

## Architecture

1. **API Layer:** FastAPI receives the ticker and builds the initial `AgentState`.
2. **Parallel Research (fan-out from `START`):**
   - `fundamentals_analyst`: Fetches PE ratio, market cap, revenue growth, profit margins, and debt-to-equity via `yfinance`, then summarizes financial health.
   - `news_analyst`: Fetches recent headlines via `yfinance` and summarizes market sentiment.
3. **Bull vs. Bear Debate (fan-in, then loop):** Once both research nodes complete, `bull_analyst` opens the debate with a bull case grounded in the fundamentals and news summaries. `bear_analyst` responds with a rebuttal. The two alternate for up to **3 rounds**, each one responding directly to the other's previous argument.
4. **Judge Agent:** After the final round, `judge_analyst` reviews the entire debate transcript and produces a verdict in a fixed format:
   ```
   VERDICT: [BUY / HOLD / SELL]
   RATIONALE: [reasoning that references specific arguments from the debate]
   ```
5. **Final Output:** The verdict is added to the state, the graph reaches the `END` node, and the unified JSON response (research summaries, full debate history, and verdict) is returned to the client.

```
                 ┌─────────────────────┐
      START ───▶ │ fundamentals_analyst │──┐
           │      └─────────────────────┘  │
           │                                ▼
           │      ┌─────────────────────┐  bull_analyst
           └───▶  │    news_analyst      │──┘      │
                  └─────────────────────┘          ▼
                                              bear_analyst
                                                    │
                                     (loop up to 3 rounds)
                                                    │
                                                    ▼
                                              judge_analyst ───▶ END
```

## Project Structure

```
app/
├── agents/
│   ├── fundamentals_analyst.py   # Summarizes financial metrics
│   ├── news_analyst.py           # Summarizes recent headlines
│   ├── bull_analyst.py           # Argues the bull case
│   ├── bear_analyst.py           # Argues the bear case
│   └── judge.py                  # Weighs the debate, issues a verdict
├── core/
│   └── config.py                 # Settings (Groq API key, etc.)
├── graph/
│   ├── state.py                  # Shared AgentState (TypedDict)
│   └── pipeline.py               # LangGraph wiring of the agents above
├── retrieval/
│   ├── fundamentals.py           # yfinance metrics fetcher
│   └── news.py                   # yfinance headline fetcher
├── schemas/
│   └── recommendation.py         # Request/response models
├── services/
│   └── llm_client.py             # Groq chat completion wrapper
└── main.py                       # FastAPI app (/health, /recommend, /recommend/stream)
```

## Development & Testing

```bash
# Run the test suite
pytest -v

# Lint and format code
ruff check .
black .
```

*Note: The GitHub Actions pipeline (`.github/workflows/ci.yml`) automatically enforces `ruff` and `black` checks on all PRs.*

## Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.