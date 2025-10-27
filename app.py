# python
from fastapi import FastAPI, HTTPException, Depends, Response, Request, Header
from pydantic import BaseModel
from typing import Optional, Dict, Any
import socket
import httpx

app = FastAPI(title="Git+Networking REST Demo")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


DB: Dict[int, dict] = {}
SEQ = 0


def auth(x_api_key: Optional[str] = Header(None)):
    # simple demo auth: require header X-API-Key: secret
    if x_api_key != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return list(DB.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    return DB[item_id]


@app.post("/items", status_code=201)
def create_item(item: Item):
    global SEQ
    SEQ += 1
    obj = {"id": SEQ, **item.dict()}
    DB[SEQ] = obj
    return obj


@app.put("/items/{item_id}")
def replace_item(item_id: int, new_item: Item):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    DB[item_id] = {"id": item_id, **new_item.dict()}
    return DB[item_id]


@app.patch("/items/{item_id}")
def patch_item(item_id: int, fields: Dict[str, Any]):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    for k, v in fields.items():
        if k in ("name", "description", "price"):
            DB[item_id][k] = v
    return DB[item_id]


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    del DB[item_id]
    return Response(status_code=204)


@app.get("/ip", dependencies=[Depends(auth)])
async def my_ip():
    async with httpx.AsyncClient(timeout=5) as client:
        r = await client.get("https://api.ipify.org?format=json")
    return {"public_ip": r.json().get("ip")}


@app.get("/resolve", dependencies=[Depends(auth)])
def resolve(host: str):
    try:
        return {"host": host, "ip": socket.gethostbyname(host)}
    except socket.gaierror:
        raise HTTPException(status_code=400, detail="DNS resolution failed")


@app.get("/ping", dependencies=[Depends(auth)])
def tcp_ping(host: str, port: int = 80, timeout: float = 1.5):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return {"host": host, "port": port, "reachable": True}
    except Exception:
        return {"host": host, "port": port, "reachable": False}
    finally:
        s.close()


@app.get("/headers", dependencies=[Depends(auth)])
def echo_headers(req: Request):
    return {k: v for k, v in req.headers.items()}


@app.get("/search", dependencies=[Depends(auth)])
def search_items(q: str):
    ql = q.lower
    return [it for it DB.values() if ql in it["name"].lower()]


