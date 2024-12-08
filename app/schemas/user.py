from datetime import datetime

from pydantic import ConfigDict

from app.base.schemas import BaseSchema


class UserOut(BaseSchema):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserProfileDTO(BaseSchema):
    id: int
    email: str
    city: str
