from fastapi import APIRouter, Depends
from app.passwords.dao import PasswordDAO
from app.passwords.rb import RBPassword
from app.passwords.shemas import PPassword, PPasswordAdd, PPasswordUpdateRequest

router = APIRouter(prefix="/passwords", tags=["passwords"])

@router.get("/", summary="get all passwords")
async def get_all_passwords(request_body: RBPassword = Depends()) -> list[PPassword]:
        return await PasswordDAO.find_all(**request_body.to_dict())


@router.get("/{id:int}", summary="Получить один пароль по id")
async def get_password_by_id(id: int) -> PPassword | dict:
    result = await PasswordDAO.find_full_data(id)
    if result is None:
        return {'message': f'Нет пароля с таким ID, ID-{id} не найден'}
    return result


@router.get("/by_filter", summary="Получить один пароль по фильтру")
async def get_password_by_filter(request_body: RBPassword = Depends()) -> PPassword | dict:
    result = await PasswordDAO.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {'message': f'Нет пароля с такими параметрами'}
    return result


@router.post("/add_password/")
async def add_password(password: PPasswordAdd) -> dict:
    check = await PasswordDAO.add(**password.dict())
    if check:
        return {"message": "Пароль успешно добавлен!", "пароль": password}
    else:
        return {"message": "Ошибка при добавлении пароля!"}


@router.put("/update_password", summary="Обновить пароль")
async def update_password(request: PPasswordUpdateRequest) -> dict:
    # Преобразуем фильтры и обновления в словари
    filters = request.filters.dict(exclude_none=True)
    updates = request.updates.dict(exclude_none=True)

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
async def delete_major(id: int) -> dict:
    check = await PasswordDAO.delete(id=id)
    if check:
        return {"message": f"Пароль с ID {id} удален!"}
    else:
        return {"message": "Ошибка при удалении пароля!"}