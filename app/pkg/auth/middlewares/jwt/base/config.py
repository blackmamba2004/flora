from dataclasses import dataclass
from datetime import timedelta


@dataclass
class JWTConfig:
    secret: str
    algorithm: str
    access_token_ttl: timedelta = None
    refresh_token_ttl: timedelta = None
