from fastapi import  HTTPException, status, Request
from fastapi import Depends
from app.database import async_session_maker
from app.users.auth import get_current_user
from app.users.models import User
from sqlalchemy import update as sqlalchemy_update
from app.users.schemas import PUserChangeRole
from jose import JWTError



async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.is_admin:
        return current_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Недостаточно прав!')


async def change_admin_status(user_id: int, new_status: bool, current_user: User):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав!")

    try:
        async with  async_session_maker() as session:
            stmt = (
                sqlalchemy_update(User)
                .where(User.id == user_id)
                .values(is_admin=new_status)
                .returning(User)
            )


            result = await session.execute(stmt)
            updated_user = result.fetchone()
            await session.commit() # Подтвердите изменения

            if updated_user is None:
                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден")

            if updated_user:
                updated_user_data = PUserChangeRole.from_orm(
                    updated_user[0])
                return {"message": f"Статус пользователя {user_id} обновлен до {new_status}",
                        "updated_user": updated_user_data}
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден")

    except Exception as e:
        print(f"Error updating admin status: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="не удалось обновить статус")



async def get_current_user_optional(request: Request) -> User | None:
    try:
        return await get_current_user(request)
    except JWTError:
        return None
    except Exception:
        return None