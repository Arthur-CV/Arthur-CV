from enum import Enum
from typing import Annotated
from fastapi import Path, APIRouter


router = APIRouter(prefix="/Shelf", tags=["Select_shelf"])


class Shelf(str, Enum):
    Shelf_1 = 'Shelf_30kg'
    Shelf_2 = 'Shelf_20kg'
    Shelf_3 = 'Shelf_10kg'


@router.get('/Shelf/storage/{type}/comment')
def get_storage_type(storage: Shelf):
    return {'message': f'storage type {type}'}


@router.get("/Shelf/{one_id}/")
def get_one_shelf(one_id: Annotated[int, Path(ge=0, le=30)]):
    return {
        "shelf": {
            "id": one_id,
        },
    }


@router.get("/Shelf/{two_id}/")
def get_two_shelf(two_id: Annotated[int, Path(ge=0, le=20)]):
    return {
        "shelf": {
            "id": two_id,
        },
    }


@router.get("/Shelf/{three_id}/")
def get_three_shelf(three_id: Annotated[int, Path(ge=0, le=10)]):
    return {
        "shelf": {
            "id": three_id,
        },
    }