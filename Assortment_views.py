from fastapi import APIRouter
from enum import Enum

router = APIRouter(prefix="/shelf", tags=['Select_product'])

class Assortment(str, Enum):
    coffee = 'coffee'
    cookies = 'cookies'
    add = 'other'


@router.post('/{Product}/')
def post_assortment(Product: Assortment):
    return {'message': f'assortment {type}'}