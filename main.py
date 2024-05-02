import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from enum import Enum
from sqlalchemy.engine.base import Engine
from typing import Optional, Annotated
from fastapi import APIRouter, Query, Path, Depends


app = FastAPI(
    title="Office Management App"
)


class Workname(BaseModel):
    email: EmailStr
    Name: str
    Role: str
    published: Optional[bool]


@app.get('/Office/{id}/comment', tags=['Put the products on the shelf'])
def hello(name: str = "Enter your name"):
    name = name.strip().title()
    return {'message': f"Put the products on the shelf {name}!"}


@app.post('/Office/', tags=['Office_worker_put_products'])
def create_user(User: Workname):
    return {
        "message": "User created successfully!",
        "email": User.email,
    }


class Shelf(str, Enum):
    Shelf_1 = 'Shelf_10kg'
    Shelf_2 = 'Shelf_20kg'
    Shelf_3 = 'Shelf_30kg'


@app.get('/Shelf/storage/{type}/comment', tags=['Select_shelf'])
def get_storage_type( storage: Shelf):
    return {'message': f'storage type {type}'}


@app.get("/Shelf/{one_id}/", tags=['Select_shelf'])
def get_one_shelf(one_id: Annotated[int, Path(ge=0, le=30)]):
    return {
        "shelf": {
        "id": one_id,
        },
    }


@app.get("/Shelf/{two_id}/", tags=['Select_shelf'])
def get_two_shelf(two_id: Annotated[int, Path(ge=0, le=20)]):
    return {
        "shelf": {
        "id": two_id,
        },
    }


@app.get("/Shelf/{three_id}/", tags=['Select_shelf'])
def get_three_shelf(three_id: Annotated[int, Path(ge=0, le=10)]):
    return {
        "shelf": {
        "id": three_id,
        },
    }


class Assortment(str, Enum):
    coffee = 'coffee'
    cookies = 'cookies'
    add = 'other'


@app.post('/shelf/{Product}/', tags=['Select_product'])
def post_assortment(Product: Assortment):
    return {'message': f'assortment {type}'}


@app.post("/Worker/{Product}/", tags=['Weight_product(Kg)'])
def sum_total_weight_Kg_on_shelves(a: int , b: int , c: int):
    return {
        "coffee": a,
        "cookies": b,
        "other": c,
        "result": a + b + c,
    }


# models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
