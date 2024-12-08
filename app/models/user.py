from sqlalchemy.orm import Mapped, mapped_column

from app.base.user import BaseUser


class User(BaseUser):
    city: Mapped[str] = mapped_column(default="Краснодар")
