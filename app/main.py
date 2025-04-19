from fastapi import FastAPI
from app.passwords.router import router as router_passwords

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Hello World"}

app.include_router(router_passwords)