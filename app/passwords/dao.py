from sqlalchemy import select

from app.dao.base import BaseDao
from app.database import async_session_maker
from app.passwords.models import Password

class PasswordDAO(BaseDao):
    model = Password

    @classmethod
    async def find_full_data(cls, password_id: int):
        async with async_session_maker() as session:
            query_password = select(cls.model).filter_by(id=password_id)
            result_password = await session.execute(query_password)
            password_info = result_password.scalar_one_or_none()

            if not password_info:
                return None

            password_data = password_info.to_dict()

            return password_data
