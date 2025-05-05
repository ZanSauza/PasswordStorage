from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, validator, ConfigDict


class PPassword(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    site: str = Field(default=..., description="Ссылка ресурса")
    user_name: str = Field(default=..., description="Логин")
    password: str = Field(default=..., description="Пароль")
    email: Optional[EmailStr] = Field(None, description="email (необязательное поле)")
    phone_number: Optional[str] = Field(None, description="Номер телефона в международном формате")
    note: Optional[str] = Field(None, description="примечание (необязательное поле)")

    @validator("phone_number")
    def validate_phone_number(cls, value):
        if value is not None and not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value


class PPasswordAdd(BaseModel):
    site_name: str = Field(default=..., description="Имя ресурса")
    site: str = Field(default=..., description="Ссылка ресурса")
    user_name: str = Field(default=..., description="Логин")
    password: str = Field(default=..., description="Пароль")
    email: Optional[EmailStr] = Field(None, description="email (необязательное поле)")
    phone_number: Optional[str] = Field(None, description="Номер телефона в международном формате")
    note: Optional[str] = Field(None, description="примечание (необязательное поле)")
    user_id: Optional[int] = Field(None, exclude=True)


class PPasswordFilter(BaseModel):
    """Модель для фильтрации пароля"""
    id: int


class PPasswordUpdateData(BaseModel):
    """Модель для обновления полей пароля"""
    site: str = Field(default=..., description="Ссылка ресурса")
    user_name: str = Field(default=..., description="Логин")
    password: str = Field(default=..., description="Пароль")
    email: Optional[EmailStr] = Field(None, description="email (необязательное поле)")
    phone_number: Optional[str] = Field(None, description="Номер телефона в международном формате")
    note: Optional[str] = Field(None, description="примечание (необязательное поле)")

class PPasswordUpdateRequest(BaseModel):
    """Модель для запроса обновления пароля"""
    filters: PPasswordFilter
    updates: PPasswordUpdateData

