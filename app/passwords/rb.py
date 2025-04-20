

class RBPassword:
    def __init__(self,
                 password_id: int | None = None,
                 username : str | None = None,
                 email: str | None = None):
        self.id = password_id
        self.username = username
        self.email = email


    def to_dict(self) -> dict:
        data = {"id": self.id, "username": self.username, "email": self.email}

        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data