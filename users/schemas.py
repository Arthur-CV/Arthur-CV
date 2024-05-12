from typing import Optional
from pydantic import BaseModel, EmailStr


class Product(BaseModel):
    email: EmailStr
    Name: str
    Role: str
    published: Optional[bool]
