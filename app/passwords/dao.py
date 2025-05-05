from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.passwords.models import Password

from sqlalchemy import select
from sqlalchemy.orm import selectinload

class PasswordDAO(BaseDAO):
    model = Password

    @classmethod
    async def find_full_data(cls, password_id: int):
        async with async_session_maker() as session:
            query_password = select(cls.model).filter_by(id=password_id)
            result_password = await session.execute(query_password)
            password_info = result_password.scalar_one_or_none()

            if not password_info:
                return None

            return password_info.to_dict()

    @classmethod
    async def find_all(cls, **filters):
        async with async_session_maker() as session:
            stmt = select(cls.model)
            if filters:
                stmt = stmt.filter_by(**filters)
            result = await session.execute(stmt)
            records = result.scalars().all()
            return [record.to_dict() for record in records]

    @classmethod
    async def find_one_or_none(cls, **filters):
        async with async_session_maker() as session:
            stmt = select(cls.model).filter_by(**filters)
            result = await session.execute(stmt)
            record = result.scalar_one_or_none()
            return record.to_dict() if record else None
