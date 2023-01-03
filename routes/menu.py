from fastapi import APIRouter
import json
from dependencies import Dependencies

router = APIRouter()

@router.get("/menu")
async def get_menu():
    food_to_list = []
    food_to_list.append(Dependencies.read_json('db/bebidas_quentes/bebidas_quentes.json'))
    food_to_list.append(Dependencies.read_json('db/bebidas_geladas/bebidas_geladas.json'))
    return food_to_list