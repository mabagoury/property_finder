import uuid

from fastapi_users import schemas
from pydantic import BaseModel


# FastAPI_Users Schemas
class UserRead(schemas.BaseUser[int]):
    username: str
    age: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    age: int
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    age: int


# Other Schemas
class PropertyUpdate(BaseModel):
    title: str = None
    description: str = None
    address: str = None
