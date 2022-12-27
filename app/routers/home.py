from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def homePage():
    return {
        "This is": "Home Page"
    }