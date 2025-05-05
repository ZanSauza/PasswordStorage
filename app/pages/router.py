from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.testing.pickleable import User

from app.passwords.dao import PasswordDAO
from app.passwords.router import get_all_passwords
from app.users.auth import get_current_user

router = APIRouter(prefix='/pages', tags=['frontend'])
templates = Jinja2Templates(directory='app/templates')


@router.get("/passwords/", response_class=HTMLResponse)
async def get_passwords_page(request: Request, user: User = Depends(get_current_user)):
    passwords = await PasswordDAO.find_all(user_id=user.id)
    return templates.TemplateResponse(name="passwords.html", context={"request": request, "passwords": passwords})


@router.get('/login')
async def get_students_html(request: Request):
    return templates.TemplateResponse(name='login_form.html', context={'request': request})

@router.get('/register')
async def get_students_html(request: Request):
    return templates.TemplateResponse(name='register_form.html', context={'request': request})