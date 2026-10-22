from fastapi import FastAPI

app = FastAPI(title="Podcast Editor API")

@app.get("/health")
def health() -> dict[str, str]:
    """Return a lightweight status response for local development."""
    return {"status": "ok"}
