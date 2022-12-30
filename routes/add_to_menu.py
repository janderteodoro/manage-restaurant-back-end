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
async def add_to_menu(new_food: Food):
    file = f'db/{new_food.group}/{new_food.group}.json'.replace(' ', '_')
    is_new = Dependencies.verify_food(filename=file, new_food_name=new_food.name)
    print(is_new)
