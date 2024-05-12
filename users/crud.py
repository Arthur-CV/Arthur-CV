"""
Create
Read
Update
Delete
"""

from sqlalchemy.testing.pickleable import User

from users.schemas import Product


def create_user(user_in: Product) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }
