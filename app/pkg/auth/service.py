from app.dao.user import UserDAO
from app.pkg.auth.dto import UserCredentialsDTO, AccessTokenDTO
from app.pkg.auth.middlewares.jwt.base.auth import JWTAuth
from app.pkg.auth.errors import AuthError
from app.pkg.errors import ErrorObj
from app.pkg.utils import get_sha256_hash


class AuthService:
    def __init__(self, jwt_auth: JWTAuth):
        self._jwt_auth = jwt_auth

    async def register(self, body: UserCredentialsDTO) -> tuple[AccessTokenDTO, None] | tuple[None, ErrorObj]:
        if await UserDAO.filter(email=body.email) is not None:
            return None, AuthError.get_email_occupied_error()
        
        hashed_password = get_sha256_hash(body.password)

        user = await UserDAO.create(
            email=body.email, 
            hashed_password=hashed_password
        )

        access_token = self._jwt_auth.generate_unlimited_access_token(subject=str(user.id))

        return AccessTokenDTO(access_token=access_token), None
    
    async def login(self, body: UserCredentialsDTO) -> tuple[AccessTokenDTO, None] | tuple[None, ErrorObj]:
        user = await UserDAO.filter(email=body.email, hashed_password=get_sha256_hash(body.password))

        if not user:
            return None, AuthError.get_invalid_credentials_error()
        
        access_token = self._jwt_auth.generate_unlimited_access_token(subject=str(user.id))

        return AccessTokenDTO(access_token=access_token), None
    