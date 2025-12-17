from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import json
from pathlib import Path


app1 = FastAPI(title="Items API", version="1.0.0")

DB_PATH = Path("db/shopping_list.json")
DB_PATH_backup = Path("data/backup_shopping_list.json")

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
        
def load_backup() -> None:
    try:
        with open(DB_PATH_backup, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")
    
def save_data(data: list, path) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

@app1.get2("/items")
async def list_items():
    loading = load_database()
    return loading

@app1.post2("/items/")
async def create_item2(item: Item):
    loading = load_database()
    item_id = str(len(loading)) + 1
    loading[item_id] = {"name": item.id, "description": item.name, "price": item.quantity}
    return {"messege":"Item created successfully",
            "item_id":item_id,
            "item":loading[item_id]}

@app1.get("/backup")
def list_all_backup() -> None:
    backup_db = load_backup()
    return backup_db

@app1.post("/backup/save")
def backup_database() -> None:
    origin_db = load_database()
    save_data(origin_db, DB_PATH_backup)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app1, host="0.0.0.0", port=8001)


