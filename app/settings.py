from datetime import timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.pkg.auth.middlewares.jwt.base.config import JWTConfig

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    JWT_SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_TTL: int
    REFRESH_TOKEN_TTL: int

    YANDEX_API_KEY: str
    YANDEX_MAP_DOMAIN: str = "https://geocode-maps.yandex.ru/1.x/"

    model_config = SettingsConfigDict(env_file='.env')

    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"


settings = Settings()


jwt_config = JWTConfig(
    secret=settings.JWT_SECRET_KEY,
    algorithm=settings.ALGORITHM,
    access_token_ttl=timedelta(seconds=settings.ACCESS_TOKEN_TTL),
    refresh_token_ttl=timedelta(seconds=settings.REFRESH_TOKEN_TTL),
)
