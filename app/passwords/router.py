from fastapi import APIRouter
from app.passwords.dao import PasswordDAO

router = APIRouter(prefix="/passwords", tags=["passwords"])

@router.get("/", summary="get all passwords")
async def get_all_passwords():
        return await PasswordDAO.find_all_passwords()