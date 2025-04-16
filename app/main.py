from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional
import requests



path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'passwords.json')


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/passwords")
async def get_all_passwords(username: Optional[str] = None, password_id: Optional[int] = None):
    passwords = json_to_dict_list(path_to_json)

    if username is not None:
        passwords = [p for p in passwords if p['username'] == username]

    if password_id is not None:
        passwords = [p for p in passwords if p['password_id'] == password_id]

    return passwords




