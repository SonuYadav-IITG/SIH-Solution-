
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def read_status():
    return {"api_status": "running"}

# Run with: uvicorn api_server:app --reload
