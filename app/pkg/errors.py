from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorObj(BaseModel):
    type: str
    message: str


def get_error_response(error: ErrorObj, status: int = 400) -> JSONResponse:
    return JSONResponse(
        content={
            'type': error.type,
            'message': error.message,
        },
        status_code=status,
    )


def get_bad_request_error_response(error: ErrorObj) -> JSONResponse:
    return get_error_response(error, status=400)