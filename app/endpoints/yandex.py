import aiohttp
from fastapi import APIRouter, Query

from app.settings import settings


router = APIRouter(prefix="/yandex-map", tags=["API Яндекс Карт"])

@router.get(
    path="/search",
    name="Найти на карте объект по координатам"
)
async def get_object_on_map(
    lat: float = Query(...),
    lon: float = Query(...)
):
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.YANDEX_MAP_DOMAIN, params={
                "apikey": settings.YANDEX_API_KEY,
                "geocode": f"{lon},{lat}",
                "kind": "street", 
                "format": "json"
            }) as response:
            return await response.json()
