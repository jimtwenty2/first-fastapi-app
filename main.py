from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    text: str = 'hi'
    is_done: bool = False

app = FastAPI()

@app.get('/')
def root() -> dict:
    return {
        "greeting":"Hello, World!"
    }

items = []


# @app.get('/items') 
# def get_items() -> dict:
#     return {
#         "items": items
#     }

@app.get('/items')
def list_items(limit: int=10):
    return items[0:limit]

@app.get('/items/{item_id}')
def get_item_id(item_id: int) -> Item:

    if item_id - 1 > len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found.")
    
    item = items[item_id-1]
    return item

@app.post('/items')
def add_item(item: Item):
    items.append(item)
    return items

