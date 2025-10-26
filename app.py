from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(title="Git+Networking REST Demo")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


DB: Dict[int, dict] = {}
SEQ = 0


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return list(DB.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(404, "Item not found")


@app.post("/items", status_code=201)
def create_item(item: Item):
    global SEQ
    SEQ += 1
    obj = {"id": SEQ, **item.dict()}
    DB[SEQ] = obj
    return obj

    