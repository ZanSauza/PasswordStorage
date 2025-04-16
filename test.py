import requests

def get_passwords_with_param_requests(username: str = None, password_id: int = None):
    url = 'http://127.0.0.1:8000/passwords'
    params = {}
    if username:
        params['username'] = username
    if password_id:
        params['password_id'] = password_id
    response = requests.get(url, params=params)
    return response.json()


passwords = get_passwords_with_param_requests(None, 1)
for password in passwords:
    print(password)