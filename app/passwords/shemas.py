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
    email: EmailStr = Field(default=..., description="email (необязательное поле)")
    phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
    note: str = Field(default=..., description="примечание (необязательное поле)")


    @validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value


class PPasswordAdd(BaseModel):
    site: str = Field(default=..., description="Ссылка ресурса")
    user_name: str = Field(default=..., description="Логин")
    password: str = Field(default=..., description="Пароль")
    email: EmailStr = Field(default=..., description="email (необязательное поле)")
    phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
    note: str = Field(default=..., description="примечание (необязательное поле)")
