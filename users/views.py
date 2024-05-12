from fastapi import APIRouter
from users import crud
from users.schemas import Product


router = APIRouter(prefix="/Office", tags=["Office_worker_put_products"])


@router.get("/{id}/")
def hello(name: str = "Enter your name"):
    name = name.strip().title()
    return {"message": f"Put the products on the shelf {name}!"}


@router.post("/")
def create_user(user: Product):
    return crud.create_user(user_in=user)
