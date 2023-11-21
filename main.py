from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!"
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_users(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }

@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
    }


@app.get("/items/")
def list_items():
    return [
        "item1",
        "item2",
        "item3",
        ]


@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}



@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item_id": {
            "id": item_id,
        }
    }





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)