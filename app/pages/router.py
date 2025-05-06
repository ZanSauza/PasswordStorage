from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.users.models import User
from app.passwords.dao import PasswordDAO
from app.passwords.router import get_all_passwords
from app.users.auth import get_current_user
from fastapi.responses import RedirectResponse


router = APIRouter(prefix='/pages', tags=['frontend'])
templates = Jinja2Templates(directory='app/templates')





@router.get("/passwords/", response_class=HTMLResponse)
async def get_passwords_page(request: Request, user: User = Depends(get_current_user)):
    passwords = await PasswordDAO.find_all(user_id=user.id)
    return templates.TemplateResponse(name="passwords.html", context={"request": request, "passwords": passwords, "user": user })


@router.get('/login')
async def get_login_page(request: Request):
    return templates.TemplateResponse(name='login_form.html', context={'request': request})

@router.get('/register')
async def get_register_page(request: Request):
    return templates.TemplateResponse(name='register_form.html', context={'request': request})

@router.post('/logout', name='logout')
async def logout():
    response = RedirectResponse(url="/pages/login", status_code=303)
    response.delete_cookie("access_token")  # Или другое имя, если ты используешь другое
    return response