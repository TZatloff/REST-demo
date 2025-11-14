from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, constr
from typing import Optional, List, Dict
from hashlib import md5
import json

app = FastAPI(title="Books API (REST demo)")


class BookIn(BaseModel):
    title: constr(min_length=1, strip_whitespace=True)
    author: constr(min_length=1, strip_whitespace=True)


class BookOut(BookIn):
    id: int
    pass


# In-memory “DB” for demo only
DB: Dict[int, BookIn] = {}
NEXT_ID = 1


# --------- Simple Auth (Bearer token demo) ---------
def get_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = authorization.split(" ", 1)[1]
    if token != "demo-token":  # never hardcode in real apps
        raise HTTPException(status_code=403, detail="Forbidden")
    return token


# --------- Helpers ---------
def make_etag(obj) -> str:
    body = json.dumps(obj, sort_keys=True).encode()
    return md5(body).hexdigest()


# --------- Routes ---------
@app.get("/books", response_model=List[BookIn])
def list_books():
    # Cacheable collection (weak demo)
    return list(DB.values())


@app.post("/books", response_model=BookIn, status_code=201, dependencies=[Depends(get_token)])
def create_book(book: BookIn):
    global NEXT_ID
    new = BookOut(id=NEXT_ID, **book.model_dump())
    DB[NEXT_ID] = new
    NEXT_ID += 1
    return new


@app.get("/books/{book_id}", response_model=BookIn)
def get_book(book_id: int, if_none_match: Optional[str] = Header(None)):
    book = DB.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Not found")
    etag = make_etag(book.model_dump())
    # Simple conditional GET using ETag
    if if_none_match == etag:
        # FastAPI doesn't have a built-in 304 helper; raise for brevity
        # In practice, set status_code=304 with empty body.
        raise HTTPException(status_code=304, detail="Not Modified")
    # You can set headers via Response, but we keep it simple for entry level
    return book


@app.put("/books/{book_id}", response_model=BookIn, dependencies=[Depends(get_token)])
def update_book(book_id: int, book: BookIn):
    if book_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    DB[book_id] = BookOut(id=book_id, **book.model_dump())
    return DB[book_id]


@app.patch("/books/{book_id}", response_model=BookIn, dependencies=[Depends(get_token)])
def patch_book(book_id: int, book: BookIn):
    existing = DB.get(book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Not found")
    updated_data = existing.model_dump()
    update_data = book.model_dump(exclude_unset=True)
    updated_data.update(update_data)
    DB[book_id] = BookOut(id=book_id, **updated_data)
    return DB[book_id]


@app.delete("/books/{book_id}", status_code=204, dependencies=[Depends(get_token)])
def delete_book(book_id: int):
    if book_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    del DB[book_id]
    return None
