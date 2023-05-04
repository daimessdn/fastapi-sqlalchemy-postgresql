from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# creating the base model


class Item(BaseModel):  # serializer (?)
    id: int
    name: str
    description: str
    price: int
    on_stock: bool


app = FastAPI()


@app.get("/")
def index():
    return {"msg": "hello, world!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "status": "success",
        "message": "hello, %s!" % (name)
    }


@app.get("/greet")
def greet_optional(name: Optional[str] = "stranger"):
    return {
        "status": "success",
        "message": f"hello, {name}"
    }


@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "on_stock": item.on_stock
    }
