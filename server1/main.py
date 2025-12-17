from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import json
from pathlib import Path

app = FastAPI(title="Items API", version="1.0.0")

DB_PATH = Path("db/shopping_list.json")

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
    loading[item_id] = {"name": item.id, "description": item.name, "price": item.quantity}
    return {"messege":"Item created successfully",
            "item_id":item_id,
            "item":loading[item_id]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)