from fastapi import APIRouter
from app.endpoints import user, video, yandex
import app.pkg.auth.transport as auth

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(video.router)
api_router.include_router(auth.router)
api_router.include_router(yandex.router)