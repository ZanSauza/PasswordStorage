from pydantic import EmailStr


class RBPassword:
    def __init__(self,
                 password_id: int | None = None,
                 user_name : str | None = None,
                 email: str | None = None,
                 password: str | None = None,
                 phone_number: str | None = None,
                 note: str | None = None):
        self.id = password_id
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.note = note

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "note": self.note
        }


        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data