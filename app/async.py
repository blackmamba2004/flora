import asyncio
from app.dao.video import VideoDAO

async def main():
    print(await VideoDAO.destroy_all())

asyncio.run(main())