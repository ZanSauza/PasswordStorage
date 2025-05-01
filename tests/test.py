import asyncio
import httpx


async def add_major(site_url: str, user_name: str, password: str, email: str, phone_number: str, note: str):
    url = 'http://127.0.0.1:8000/passwords/add_password/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "site": site_url,
        "user_name": user_name,
        "password": password,
        "email": email,
        "phone_number": phone_number,
        "note": note
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        return response.json()


# вызов функции
response = asyncio.run(add_major(site_url="http://127.0.0.1:8000", user_name="admin2", password="<PASSWORD>", email="EMAIL1@mail.ru", phone_number="+9121111111", note="test"))
print(response)