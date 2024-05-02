from fastapi import APIRouter


router = APIRouter(tags=['Weight_product(Kg)'])


@router.post("/worker/{Product}/")
def sum_total_weight_Kg_on_shelves(a: int, b: int, c: int):
    return {
        "coffee": a,
        "cookies": b,
        "other": c,
        "result": a + b + c,
    }