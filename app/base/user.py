from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.base.fields import int_pk, str_unique, created_at, updated_at
from app.database import Base


class BaseUser(Base):
    __abstract__ = True

    id: Mapped[int_pk]
    email: Mapped[str_unique] = mapped_column(String(254))
    hashed_password: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
