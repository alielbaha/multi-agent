from fastapi import FastAPI

app = FastAPI(title = "multi agent system")

@app.get("/health")
def health():
    return {"status": "fine"}

