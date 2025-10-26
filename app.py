from fastapi import FastAPI

app = FastAPI(title="Git+Networking REST Demo")


@app.get("/health")
def health():
   return {"status": "ok"}

