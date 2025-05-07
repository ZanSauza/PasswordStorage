
class RBPassword:
    def __init__(
        self,
        user_id: int | None = None,              
        password_id: int | None = None,
        site_name: str | None = None,
        user_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone_number: str | None = None,
        note: str | None = None
    ):
        self.user_id = user_id
        self.id = password_id
        self.site_name = site_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.note = note

    def to_dict(self) -> dict:
        data = {
            "user_id": self.user_id,
            "id": self.id,
            "site_name": self.site_name,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "note": self.note
        }

        return {key: value for key, value in data.items() if value is not None}
