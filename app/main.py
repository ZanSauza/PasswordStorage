from fastapi import FastAPI
from app.passwords.router import router as router_passwords
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')


@app.get("/")
def home_page():
    return {"message": "Hello World"}


app.include_router(router_pages)
app.include_router(router_users)
app.include_router(router_passwords)
