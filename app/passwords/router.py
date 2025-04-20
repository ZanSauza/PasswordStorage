from fastapi import APIRouter, Depends
from app.passwords.dao import PasswordDAO
from app.passwords.rb import RBPassword
from app.passwords.shemas import PPassword

router = APIRouter(prefix="/passwords", tags=["passwords"])

@router.get("/", summary="get all passwords")
async def get_all_passwords(request_body: RBPassword = Depends()) -> list[PPassword]:
        return await PasswordDAO.find_all(**request_body.to_dict())