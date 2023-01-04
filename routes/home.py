from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

router = APIRouter()

@router.get("/")
async def homePage():
    return {
        "This is": "Home Page"
    }