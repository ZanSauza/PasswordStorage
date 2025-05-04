from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from app.passwords.router import get_all_passwords



router = APIRouter(prefix='/pages', tags=['frontend'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/passwords/')
async def get_passwords_html(request: Request, passwords=Depends(get_all_passwords)):
    return templates.TemplateResponse(name='passwords.html',
                                      context={'request': request, 'passwords': passwords})