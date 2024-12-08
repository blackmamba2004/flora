from pydantic import BaseModel


class UserCredentialsDTO(BaseModel):
    email: str
    password: str


class AccessTokenDTO(BaseModel):
    access_token: str