import uvicorn
from fastapi import FastAPI
from sqlalchemy.engine.base import Engine
from typing import Optional, Annotated
from fastapi import APIRouter, Query, Path, Depends
from users.views import router as users_router
from Shelf_views import router as Shelf_router
from Assortment_views import router as Assortment_router
from Worker import router as Worker_router


app = FastAPI(
    title="Office Management App"
)
app.include_router(users_router)
app.include_router(Shelf_router)
app.include_router(Assortment_router)
app.include_router(Worker_router)
# models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
