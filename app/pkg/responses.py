from pydantic import BaseModel


class ErrorOut(BaseModel):
    type: str
    message: str
