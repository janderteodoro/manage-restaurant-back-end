from fastapi import FastAPI
from routes import home, menu

app = FastAPI()

app.include_router(home.router)
app.include_router(menu.router)