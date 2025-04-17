from fastapi import FastAPI, Depends
from utils import json_to_dict_list
import os
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from typing import Optional, List
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
def add_student_handler(password: PPassword):
    password_dict = password.dict()
    check = add_password(password_dict)
    if check:
        return {"message": "Пароль успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении пароля"}




small_db = JSONDatabase(file_path='students.json')


# получаем все записи
def json_to_dict_list():
    return small_db.get_all_records()


# добавляем студента
def add_password(password: dict):
    small_db.add_records(password)
    return True


# обновляем данные по студенту
def upd_password(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


# удаляем студента
def dell_password(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True
