from fastapi import APIRouter
from pydantic import BaseModel
import json 
from dependencies import Dependencies

router = APIRouter()

class Food(BaseModel):
    group: str
    name: str
    description: str
    price: float

@router.post("/menu", name='route for add food at the menu')
async def add_to_menu(food: Food):
    file = f'db/{food.group}/{food.group}.json'
