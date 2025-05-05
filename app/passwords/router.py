from fastapi import APIRouter, Depends, HTTPException, status
from app.passwords.dao import PasswordDAO
from app.passwords.rb import RBPassword
from app.passwords.shemas import PPassword, PPasswordAdd, PPasswordUpdateRequest
from app.users.auth import get_current_user
from app.users.models import User

router = APIRouter(prefix="/passwords", tags=["passwords"])

@router.get("/", summary="get all passwords")
async def get_all_passwords(
    filters: RBPassword = Depends(),
    current_user: User = Depends(get_current_user)) -> list[PPassword]:
    filters_dict = filters.to_dict()
    filters_dict["user_id"] = current_user.id
    return await PasswordDAO.find_all(**filters_dict)



@router.get("/{id:int}", summary="Получить один пароль по id")
async def get_password_by_id(
    id: int,
    current_user: User = Depends(get_current_user)) -> PPassword | dict:
    result = await PasswordDAO.find_full_data(id)
    if result is None or result.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Нет доступа к этому паролю")
    return result


@router.get("/by_filter", summary="Получить один пароль по фильтру")
async def get_password_by_filter(
    request_body: RBPassword = Depends(),
    current_user: User = Depends(get_current_user)) -> PPassword | dict:
    filters = request_body.to_dict()
    filters["user_id"] = current_user.id
    result = await PasswordDAO.find_one_or_none(**filters)
    if result is None:
        return {'message': f'Нет пароля с такими параметрами'}
    return result


@router.post("/add_password/")
async def add_password(
    password: PPasswordAdd,
    current_user: User = Depends(get_current_user)) -> dict:
    data = password.dict()
    data["user_id"] = current_user.id

    check = await PasswordDAO.add(**data)
    if check:
        return {"message": "Пароль успешно добавлен!", "пароль": password}
    else:
        return {"message": "Ошибка при добавлении пароля!"}



@router.put("/update_password", summary="Обновить пароль")
async def update_password(
    request: PPasswordUpdateRequest,
    current_user: User = Depends(get_current_user)) -> dict:
    filters = request.filters.dict(exclude_none=True)
    filters["user_id"] = current_user.id
    updates = request.updates.dict(exclude_none=True, exclude={"user_id"})

    if not filters:
        return {"message": "Нужно передать хотя бы один фильтр поиска"}

    if not updates:
        return {"message": "Нужно передать хотя бы одно обновляемое поле"}

    updated = await PasswordDAO.update(filters, updates)

    if updated:
        return {"message": "Данные успешно обновлены"}
    else:
        return {"message": "Ошибка при обновлении"}


@router.delete("/delete/{id:int}")
async def delete_major(
    id: int,
    current_user: User = Depends(get_current_user)) -> dict:
    existing = await PasswordDAO.find_full_data(id)
    if not existing or existing.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Нет доступа к удалению")

    check = await PasswordDAO.delete(id=id)
    if check:
        return {"message": f"Пароль с ID {id} удален!"}
    else:
        return {"message": "Ошибка при удалении пароля!"}
