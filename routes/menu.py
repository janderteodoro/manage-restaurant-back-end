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

@router.get("/menu")
async def get_menu():
    food_to_list = []
    food_to_list.append(Dependencies.read_json('db/bebidas_quentes/bebidas_quentes.json'))
    food_to_list.append(Dependencies.read_json('db/bebidas_geladas/bebidas_geladas.json'))
    return food_to_list


@router.post("/menu", name='route for add food at the menu')
async def add_to_menu(new_food: Food):
    file = f'db/{new_food.group}/{new_food.group}.json'.replace(' ', '_')
    is_new = Dependencies.verify_food(filename=file, new_food_name=new_food.name)
    if not is_new:
        return {
            'statusCode': 409,
            'message': 'food already exists'
        }
    
    actual_content = Dependencies.read_json(filename=file)
    
    content = {
        'name': new_food.name,
        'description': new_food.description,
        'price': new_food.price,
        'number': 12
    }

    actual_content[new_food.group].append(content)
    content_to_write = json.dumps(actual_content)
    Dependencies.write_json(filename=file, content=content_to_write)

    return {
        'statusCode': 201,
        'message': 'Created'
    }
