from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/passwords/')
async def get_passwords_html(request: Request):
    return templates.TemplateResponse(name='passwords.html', context={'request': request})