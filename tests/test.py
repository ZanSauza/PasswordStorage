import requests
from utils import json_to_dict_list
from pydantic import  ValidationError
from typing import Optional, List


#
# def get_passwords_with_param_requests(username: str = None, password_id: int = None):
#     url = 'http://127.0.0.1:8000/passwords'
#     params = {}
#     if username:
#         params['username'] = username
#     if password_id:
#         params['password_id'] = password_id
#     response = requests.get(url, params=params)
#     return response.json()
#
#
# passwords = get_passwords_with_param_requests(None, 1)
# for password in passwords:
#     print(password)

url = "http://127.0.0.1:8000/add_student"


data = {
    "password_id": 1,
    "site": "example.com",
    "username": "myuser",
    "password": "secretpass",
    "email": "user@example.com",
    "Note": "Это тестовая запись"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())