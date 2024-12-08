from fastapi import APIRouter, Depends, Request, Security

from app.pkg.auth.middlewares.jwt.service import check_access_token, jwt_config
from app.pkg.auth.middlewares.jwt.base.auth import JWTAuth
from app.pkg.auth.service import AuthService

from app.pkg.auth.transport.requests import UserCredentialsIn
from app.pkg.auth.transport.responses import AccessTokenOut
from app.pkg.errors import get_bad_request_error_response
from app.pkg.responses import ErrorOut


router = APIRouter(prefix='/auth')


def get_auth_service() -> AuthService:
    return AuthService(jwt_auth=JWTAuth(config=jwt_config))


@router.post(
    path='/register',
    tags=['Клиентское приложение / Регистрация'],
    name='Зарегистрировать пользователя',
    responses={
        200 : {'model': AccessTokenOut},
        400 : {'model': ErrorOut}
    }
)
async def register_user(
    body: UserCredentialsIn,
    auth_service: AuthService = Depends(get_auth_service)
) -> AccessTokenOut:
    data, error = await auth_service.register(body)

    if error:
        return get_bad_request_error_response(error=error)

    return data


@router.post(
    path='/login',
    tags=['Клиентское приложение / Вход'],
    name='Войти в приложение',
    responses={
        200 : {'model': AccessTokenOut},
        400 : {'model': ErrorOut}
    }
)
async def login_user(
    body: UserCredentialsIn,
    auth_service: AuthService = Depends(get_auth_service)
) -> AccessTokenOut:
    data, error = await auth_service.login(body)

    if error:
        return get_bad_request_error_response(error=error)

    return data
