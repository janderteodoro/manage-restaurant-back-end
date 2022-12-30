from fastapi import FastAPI
from routes import home, menu, add_to_menu

app = FastAPI()

app.include_router(home.router)
app.include_router(menu.router)
app.include_router(add_to_menu.router)