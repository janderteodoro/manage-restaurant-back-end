from fastapi import APIRouter
import json
from dependencies import Dependencies

router = APIRouter()

@router.get("/menu")
async def get_menu():
    bebidas_quentes = 'db/bebidas_quentes/bebidas_quentes.json'
    bebidas_geladas = 'db/bebidas_geladas/bebidas_geladas.json'
    food_to_list = []
    food_to_list.append(Dependencies.read_json(bebidas_geladas))
    food_to_list.append(Dependencies.read_json(bebidas_quentes))
    return food_to_list