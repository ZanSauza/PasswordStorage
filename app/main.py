from http.client import HTTPException

from fastapi import FastAPI, Depends
from utils import json_to_dict_list
import os
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from typing import Optional, List, Any
from json_db_lite import JSONDatabase




path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'passwords.json')





app = FastAPI()


class PPassword(BaseModel):
    password_id: int
    site: str = Field(default=..., description="Ссылка ресурса"),
    username: str = Field(default=..., description="Логин"),
    password: str = Field(default=..., description="Пароль"),
    email: EmailStr = Field(default=..., description="email (необязательное поле)"),
    Note: str = Field(default=..., description="примечание (необязательное поле)"),


class RBPassword:
    def __init__(self, username: str = None):
        self.username: str = username




class PUpdateFilter(BaseModel):
    password_id: int

# Определение модели для новых данных пароля
class PPasswordUpdate(BaseModel):
    site: str = Field(default=..., description="Ссылка ресурса"),
    username: str = Field(default=..., description="Логин"),
    password: str = Field(default=..., description="Пароль"),
    email: EmailStr = Field(default=..., description="email (необязательное поле)"),
    Note: str = Field(default=..., description="примечание (необязательное поле)"),


class PDeleteFilter(BaseModel):
    key: str
    value: Any

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/passwords/{username}")
async def get_all_passwords_username(request_body: RBPassword = Depends()) -> List[PPassword]:
    passwords = json_to_dict_list(path_to_json)
    filtered_passwords = []
    for password in passwords:
        if password['username'] == request_body.username:
            filtered_passwords.append(password)


    return filtered_passwords



@app.post("/add_password")
def add_password_handler(password: PPassword):
    password_dict = password.dict()
    check = add_password(password_dict)
    if check:
        return {"message": "Пароль успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении пароля"}



@app.put("/update_password")
def update_password_handler(filter_password: PUpdateFilter, new_data: PPasswordUpdate):
    check = upd_password(filter_password.dict(), new_data.dict())
    if check:
        return {"message": "Пароль обновлен!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении пароля")


@app.delete("/dellete_password")
def delete_password_handler(filter_password: PDeleteFilter):
    check = dell_password(filter_password.key, filter_password.value)
    if check:
        return {"message": "Пароль удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении пароля")














small_db = JSONDatabase(file_path='passwords.json')


# получаем все записи
def json_to_dict_list():
    return small_db.get_all_records()


# добавляем пароль
def add_password(password: dict):
    small_db.add_records(password)
    return True


# обновляем пароль
def upd_password(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


# удаляем пароль
def dell_password(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True
