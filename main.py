from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root() -> dict:
    return {
        "greeting":"Hello, World!"
    }

items = []

@app.get('/items') 
def get_items() -> dict:
    return {
        "items": items
    }

@app.get('/items/{item_id}')
def get_item_id(item_id: int) -> dict:
    item = items[item_id-1]
    return {
        "item_id": item_id,
        "item": item
    }

@app.post('/items')
def add_item(item: str) -> dict:
    items.append(item)
    return {
        "items":items
    }

