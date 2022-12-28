from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/menu")
async def get_menu():
    filename = 'mock/menu.json'
    with open(filename, 'r') as f:
        menu = json.load(f)
    return menu