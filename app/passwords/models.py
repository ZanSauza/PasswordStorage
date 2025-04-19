from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true



class Password(Base):
    id: Mapped[int_pk]
    site: Mapped[str]
    user_name: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str_uniq] = mapped_column(nullable=True)
    email: Mapped[str_uniq] = mapped_column(nullable=True)
    note: Mapped[str] = mapped_column(nullable=True)



    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"user_name={self.user_name!r}")

    def __repr__(self):
        return str(self)


    def to_dict(self):
        return {
            "id": self.id,
            "site": self.site,
            "user_name": self.user_name,
            "password": self.password,
            "phone_number": self.phone_number,
            "email": self.email,
            "note": self.note,

        }
