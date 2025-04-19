from sqlalchemy import select
from app.passwords.models import Password
from app.database import async_session_maker

class PasswordDAO:
    @classmethod
    async def find_all_passwords(cls):
        async with async_session_maker() as session:
            query = select(Password)
            passwords = await session.execute(query)
            return passwords.scalars().all()