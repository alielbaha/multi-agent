# Multi-Agent Financial Analysis System

[![CI](https://img.shields.io/badge/CI-Passing-brightgreen?logo=githubactions&logoColor=white)](https://github.com/alielbaha/multi-agent/actions)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, multi-agent AI system for real-time stock analysis. Combines fundamental metrics and news sentiment using LangGraph, FastAPI, and Groq LLMs.

## Features

- **Parallel Execution:** Simultaneous fundamental and news analysis via LangGraph's fan-out pattern.
- **Intelligent Synthesis:** A dedicated Synthesizer Agent waits for parallel analyses to complete, combining them into a concise final investment recommendation (bullish, bearish, or neutral).
- **Real-Time Data:** Live stock metrics and headlines fetched via `yfinance`.
- **LLM-Powered:** AI-generated analytical summaries and final recommendations using the Groq API.
- **Production-Ready:** FastAPI backend with Pydantic validation, Docker support, and automated CI/CD.

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

## Architecture

1. **API Layer:** FastAPI receives the ticker and initializes the `AgentState`.
2. **LangGraph Pipeline:** Orchestrates a parallel workflow starting from the `START` node.
3. **Specialized Agents:**
   - `fundamentals_analyst`: Fetches PE, market cap, margins, etc., and summarizes financial health.
   - `news_analyst`: Fetches recent headlines and summarizes market sentiment.
4. **Synthesizer Agent:** Executes after the parallel agents finish (fan-in), reading their summaries from the state to generate a final 3-4 sentence investment recommendation.
5. **Final Output:** The synthesized recommendation is added to the state, and the graph reaches the `END` node, returning the unified JSON response to the client.

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