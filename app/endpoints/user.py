from fastapi import APIRouter, Security, Request

from app.pkg.auth.middlewares.jwt.service import check_access_token
from app.schemas.user import UserProfileDTO

router = APIRouter(prefix='/users', tags=['Клиентское приложение / Профиль'])


@router.get(
    path='/me',
    name='Получить профиль пользователя',
    response_model=UserProfileDTO,
    dependencies=[Security(check_access_token)]
)
async def get_me_user_info(request: Request):
    return request.state.user