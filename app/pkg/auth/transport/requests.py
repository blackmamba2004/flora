from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCredentialsIn(BaseModel):
    email: EmailStr = Field(min_length=1, max_length=254)
    password: str = Field(min_length=1)

    model_config = ConfigDict(str_strip_whitespace=True)

