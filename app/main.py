from fastapi import FastAPI, Request
from app.passwords.router import router as router_passwords
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')


@app.exception_handler(HTTPException)
async def auth_redirect_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 401:
        return RedirectResponse(url="/pages/login", status_code=HTTP_302_FOUND)
    raise exc


app.include_router(router_pages)
app.include_router(router_users)
app.include_router(router_passwords)
