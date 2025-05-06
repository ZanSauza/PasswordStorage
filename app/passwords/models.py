from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk



class Password(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    site_name: Mapped[str]
    site: Mapped[str]
    user_name: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    note: Mapped[str] = mapped_column(nullable=True)

    user = relationship("User", back_populates="passwords")




    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"user_name={self.user_name!r}")

    def __repr__(self):
        return str(self)


    def to_dict(self):
        return {
            "id": self.id,
            "site_name": self.site_name,
            "site": self.site,
            "user_name": self.user_name,
            "password": self.password,
            "phone_number": self.phone_number,
            "email": self.email,
            "note": self.note,

        }