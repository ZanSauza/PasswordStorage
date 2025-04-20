from app.dao.base import BaseDao
from app.passwords.models import Password

class PasswordDAO(BaseDao):
    model = Password
