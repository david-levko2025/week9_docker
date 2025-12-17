from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import json
from pathlib import Path

app = FastAPI(title="Items API", version="1.0.0")

DB_PATH = Path("data/db.json")

class Item(BaseModel):
    id: int
    name: str
    quantity: float

def load_database() -> Dict:
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")

@app.get("/items")
async def list_items():
    loading = load_database()
    return loading

@app.post("/items/")
async def create_item(item: Item):
    loading = load_database()
    item_id = str(len(loading)) + 1
    loading[item_id] = {"name": item.name, "description": item.description, "price": item.price}
    return {"messege":"Item created successfully",
            "item_id":item_id,
            "item":loading[item_id]}