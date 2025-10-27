from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from typing import Any

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


@app.put("/items{item_id}")
def replace_item(item_id: int, new_item: Item):
    if item_id not in DB:
        raise HTTPException(404, "Item not found")
    DB[item_id] = {"id": item_id, **new_item.dict()}
    return DB[item_id]


@app.patch("items{item_id}")
def patch_item(item_id: int, fields: dict):
    if item_id not in DB:
        raise HTTPException(404, "Item not found")
    for k, v in fields.items():
        if k in ("name", "description", "price"):
            DB[item_id][k] = v
    return DB[item_id]


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(404, "Item not found")
    del DB[item_id]
    return


